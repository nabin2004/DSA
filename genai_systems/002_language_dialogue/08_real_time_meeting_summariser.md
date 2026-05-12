# 08. Real-Time Meeting Summariser

## Objective

Transcribes, summarizes, and extracts action items from live meetings in real-time, combining speech-to-text, NLP, and meeting understanding.

## System Architecture

[Mermaid diagram - flowchart showing core components and data flow]

[3-5 sentence description of architecture]

## Technical Approach

### Key Components

- **Speech Recognition**: [description]
- **Real-time Transcription**: [description]
- **Summarization Model**: [description]
- **Action Item Extractor**: [description]

### Pipeline / Data Flow

[Detailed description of request → processing → response flow]

## Complexity Analysis

| Metric | Complexity | Notes |
|--------|-----------|-------|
| Model size | ASR: 100M-500M, Summarizer: 3B-13B | [implications] |
| Time complexity | O(audio_length) | [notes] |
| Space complexity | ~2-10GB streaming | [notes] |
| Latency target | <2s delay from speech | [real-time vs. batch] |
| Throughput target | 100-1000 concurrent streams | [per GPU/instance] |

## Pros & Cons

### Pros

- **[Pro 1]**: [1-2 sentence explanation]
- **[Pro 2]**: [1-2 sentence explanation]

### Cons

- **[Con 1]**: [1-2 sentence explanation]
- **[Con 2]**: [1-2 sentence explanation]

### Trade-offs

[1-2 paragraphs discussing key technical trade-offs]

## Real-World Applications

### Where This Pattern Appears

- **[Company/Product 1]**: [Use case]
- **[Company/Product 2]**: [Use case]

### Production Considerations

[2-3 paragraphs on scaling, failure modes, monitoring, cost]

## References & Citations

### Citation 1: Architecture & Design

**Title**: [Paper/Blog Title on Real-Time Meeting Summariser Architecture]
- **Author(s)**: [Author names]
- **Published**: [Date]
- **Link**: [https://example.com/paper1]
- **Summary**: [1-2 sentences on key technical contribution]

### Citation 2: Performance & Benchmarks

**Title**: [Performance Benchmarks for Real-Time Meeting Summariser]
- **Author(s)**: [Author names]  
- **Published**: [Date]
- **Link**: [https://example.com/paper2]
- **Summary**: [1-2 sentences on performance characteristics]

### Citation 3: Implementation Details

**Title**: [Implementation Details and Trade-offs]
- **Author(s)**: [Author names]
- **Published**: [Date]
- **Link**: [https://example.com/paper3]
- **Summary**: [1-2 sentences on practical implementation insights]

### Citation 4: Real-World Deployment

**Title**: [Production Deployment Insights]
- **Author(s)**: [Author names]
- **Published**: [Date]
- **Link**: [https://example.com/paper4]
- **Summary**: [1-2 sentences on deployment considerations]

### Reproducibility Checklist

- [ ] All claims verified against source material
- [ ] Diagram generated and renders correctly in Markdown
- [ ] Complexity figures match cited papers or benchmarks
- [ ] Real-world examples are current (within 1 year)
- [ ] Page reviewed for consistency with other skeleton pages
