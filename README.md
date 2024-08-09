# Bedrock and W&B Weave

This repository demonstrates how to use Weights and Biases (W&B) Weave with AWS Bedrock model serving. It showcases two different language models and various use cases.

## Notebooks

| Notebook | Description | Link |
| --- | --- | --- |
| `bedrock_claude_weave.ipynb` | Evaluations with Claude 3.5 Sonnet (Anthropic) | [View](bedrock_claude_weave.ipynb) |
| `bedrock_mistral_weave.ipynb` | Examples with Mistral 7B | [View](bedrock_mistral_weave.ipynb) |

## Key Features in bedrock_claude_weave.ipynb

1. **Setup and Integration**: 
   - Demonstrates how to set up and use AWS Bedrock with Claude 3.5 Sonnet.
   - Integrates Weights & Biases (W&B) Weave for logging and debugging.

2. **Model Interaction**:
   - Shows different methods to interact with Claude, including a custom function and the Anthropic Python SDK.

3. **Evaluation Framework**:
   - Implements an evaluation pipeline using the Factual Inconsistency Benchmark.
   - Uses `instructor` for structured output from Claude.

4. **Performance Comparison**:
   - Compares different versions of Claude (Haiku vs Sonnet) on the benchmark.

5. **Best Practices**:
   - Demonstrates efficient prompt engineering and response handling.
   - Shows how to use Weave for tracking experiments and model outputs.

## Getting Started

1. Clone this repository.
2. Install the required dependencies (see notebook for details).
3. Set up your AWS credentials for Bedrock access.
4. Run the `bedrock_claude_weave.ipynb` notebook to see Claude in action with W&B Weave.

## Contributing

Contributions to improve the examples or add new features are welcome. Please feel free to submit a pull request or open an issue for discussion.