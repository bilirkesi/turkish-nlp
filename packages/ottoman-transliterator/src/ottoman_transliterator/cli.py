"""
CLI for Ottoman Transliteration Pipeline
"""

import click
import json
from pathlib import Path

from .pipeline import OttomanTransliterationPipeline, OttomanPipelineConfig


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """Osmanlica - Ottoman Turkish Transliteration Pipeline"""
    pass


@cli.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.option("--output", "-o", type=click.Path(), default=None, help="Output file")
@click.option("--model", "-m", default="deepseek-v4-flash", help="Model to use")
@click.option(
    "--mode",
    "-M",
    type=click.Choice(["hybrid", "neural", "nlp"]),
    default="hybrid",
    help="Transliteration mode",
)
@click.option("--api-key", "-k", default=None, help="DeepSeek API key")
@click.option("--json", is_flag=True, help="Output as JSON")
def translate(input_file, output, model, mode, api_key, json):
    """Transliterate Ottoman Turkish text to Modern Turkish."""
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    config = OttomanPipelineConfig(
        model=model,
        api_key=api_key,
    )
    pipeline = OttomanTransliterationPipeline(config)

    result = pipeline.transliterate(text, mode=mode)

    if json:
        output_data = result.to_dict()
        if output:
            with open(output, "w", encoding="utf-8") as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)
        else:
            click.echo(json.dumps(output_data, indent=2, ensure_ascii=False))
    else:
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(result.modern_turkish)
        else:
            click.echo(result.modern_turkish)

    click.echo(f"\nConfidence: {result.confidence:.2%}", err=True)
    click.echo(f"Method: {result.metrics.get('method', 'unknown')}", err=True)


@cli.command()
@click.argument("input_dir", type=click.Path(exists=True))
@click.option("--output", "-o", type=click.Path(), default=None)
@click.option("--model", "-m", default="deepseek-v4-flash")
@click.option("--workers", "-w", default=4, help="Number of parallel workers")
def batch(input_dir, output, model, workers):
    """Batch transliterate all .txt files in directory."""
    config = OttomanPipelineConfig(model=model)
    pipeline = OttomanTransliterationPipeline(config)

    txt_files = list(Path(input_dir).glob("*.txt"))
    click.echo(f"Found {len(txt_files)} files to process")

    results = []
    for i, txt_file in enumerate(txt_files, 1):
        click.echo(f"[{i}/{len(txt_files)}] Processing {txt_file.name}...")
        with open(txt_file, "r", encoding="utf-8") as f:
            text = f.read()

        result = pipeline.transliterate(text)
        results.append({
            "file": txt_file.name,
            "result": result.to_dict(),
        })

    if output:
        output_path = Path(output)
        output_path.mkdir(parents=True, exist_ok=True)
        for r in results:
            out_file = output_path / f"{r['file']}.json"
            with open(out_file, "w", encoding="utf-8") as f:
                json.dump(r, f, indent=2, ensure_ascii=False)
        click.echo(f"Results saved to {output_path}")
    else:
        for r in results:
            click.echo(f"\n{r['file']}:")
            click.echo(r['result']['modern_turkish'][:200] + "...")


@cli.command()
@click.option("--dataset", "-d", default="osmanlica-bench", help="Dataset name")
@click.option("--model", "-m", default="deepseek-v4-flash")
def benchmark(dataset, model):
    """Run benchmark on test dataset."""
    click.echo(f"Running benchmark on {dataset} with {model}...")
    # Implementation would load dataset and run evaluation
    click.echo("Benchmark completed (placeholder)")


@cli.command()
def info():
    """Show pipeline information."""
    click.echo("Osmanlica Transliteration Pipeline v1.0.0")
    click.echo("Author: Bilirkesi AI Team")
    click.echo("License: MIT")
    click.echo("\nSupported models:")
    click.echo("  - deepseek-v4-flash (recommended)")
    click.echo("  - deepseek-v3.2")
    click.echo("  - qwen3-32b")
    click.echo("\nFeatures:")
    click.echo("  - Hybrid neural + NLP transliteration")
    click.echo("  - Confidence scoring")
    click.echo("  - Uncertainty marking")
    click.echo("  - NER/POS annotations")


if __name__ == "__main__":
    cli()
