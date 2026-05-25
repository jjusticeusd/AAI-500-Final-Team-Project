param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]] $JupyterArgs
)

uv add --dev ipykernel
uv run --with jupyter jupyter lab @JupyterArgs
