"""GenAI system definitions for all 22 interview topics."""

from dsapython.template_generator import GenAISystem, ComplexityMetrics


# Define all 22 GenAI systems
ALL_SYSTEMS = [
    # Foundations (2 systems)
    GenAISystem(
        number=2,
        title="Gmail Smart Compose",
        category="Foundations",
        objective="Predicts and suggests the next words in email drafts using an on-device ML model, demonstrating real-time language prediction at scale for billions of users.",
        key_components=["Encoder", "Language Model", "Sampling Layer", "On-device Inference Engine"],
        complexity_metrics=ComplexityMetrics(
            model_size="10-100M parameters (on-device)",
            time_complexity="O(seq_len) per token",
            space_complexity="~50-200MB on device",
            latency_target="p95 <50ms",
            throughput_target="1000s of requests/s (aggregated)"
        )
    ),
    GenAISystem(
        number=3,
        title="Google Translate",
        category="Foundations",
        objective="Translates text between 100+ languages using sequence-to-sequence models, representing a foundational system that combines encoder-decoder architecture with attention mechanisms.",
        key_components=["Encoder", "Decoder", "Attention Mechanism", "Vocabulary Mappings", "Beam Search"],
        complexity_metrics=ComplexityMetrics(
            model_size="200M-500M parameters (server-side)",
            time_complexity="O(seq_len²) with attention",
            space_complexity="~1-2GB per model",
            latency_target="p95 <200ms",
            throughput_target="1000-10k requests/s"
        )
    ),
    
    # Language & Dialogue (5 systems)
    GenAISystem(
        number=4,
        title="ChatGPT: Personal Assistant Chatbot",
        category="Language & Dialogue",
        objective="A conversational AI that understands context, maintains multi-turn dialogues, and generates coherent responses using large language models fine-tuned with RLHF.",
        key_components=["Large Language Model", "Prompt Formatting", "Context Management", "RLHF Training Pipeline"],
        complexity_metrics=ComplexityMetrics(
            model_size="7B-70B parameters",
            time_complexity="O(seq_len²)",
            space_complexity="~14-140GB (FP16)",
            latency_target="p95 <1s per message",
            throughput_target="20-100 req/s per GPU"
        )
    ),
    GenAISystem(
        number=5,
        title="Retrieval Augmented Generation",
        category="Language & Dialogue",
        objective="Combines information retrieval with generation to ground LLM outputs in external knowledge bases, improving accuracy and reducing hallucination.",
        key_components=["Query Encoder", "Dense Retriever", "Ranking Model", "LLM", "Fusion Module"],
        complexity_metrics=ComplexityMetrics(
            model_size="Retriever: 100M-1B, LLM: 7B-70B",
            time_complexity="O(n) retrieval + O(seq_len²) generation",
            space_complexity="Vector index: 10GB-1TB, LLM: 14-140GB",
            latency_target="p95 <2s (retrieval + generation)",
            throughput_target="10-50 req/s per GPU"
        )
    ),
    GenAISystem(
        number=6,
        title="Code Generation Assistant",
        category="Language & Dialogue",
        objective="Generates, completes, and refactors code in multiple programming languages, trained on code datasets and fine-tuned for software engineering tasks.",
        key_components=["Code LLM", "Syntax Highlighter", "Testing Framework", "Version Control Integration"],
        complexity_metrics=ComplexityMetrics(
            model_size="1B-100B parameters",
            time_complexity="O(seq_len²)",
            space_complexity="~2-200GB",
            latency_target="p95 <1s per completion",
            throughput_target="50-500 req/s"
        )
    ),
    GenAISystem(
        number=7,
        title="Document Q&A over PDF/Enterprise Corpus",
        category="Language & Dialogue",
        objective="Answers questions by searching and comprehending large document collections, combining dense retrieval with reading comprehension over enterprise data.",
        key_components=["PDF Parser", "Text Chunker", "Embedding Model", "Vector DB", "Re-ranker", "Reader LLM"],
        complexity_metrics=ComplexityMetrics(
            model_size="Embeddings: 100M-1B, Reader: 7B-13B",
            time_complexity="O(corpus_size) search + O(doc_len²) reading",
            space_complexity="Vector index: proportional to corpus",
            latency_target="p95 <3s",
            throughput_target="5-20 req/s"
        )
    ),
    GenAISystem(
        number=8,
        title="Real-Time Meeting Summariser",
        category="Language & Dialogue",
        objective="Transcribes, summarizes, and extracts action items from live meetings in real-time, combining speech-to-text, NLP, and meeting understanding.",
        key_components=["Speech Recognition", "Real-time Transcription", "Summarization Model", "Action Item Extractor"],
        complexity_metrics=ComplexityMetrics(
            model_size="ASR: 100M-500M, Summarizer: 3B-13B",
            time_complexity="O(audio_length)",
            space_complexity="~2-10GB streaming",
            latency_target="<2s delay from speech",
            throughput_target="100-1000 concurrent streams"
        )
    ),
    
    # Multimodal Image (7 systems)
    GenAISystem(
        number=9,
        title="Image Captioning",
        category="Multimodal Image",
        objective="Generates descriptive text for images by combining vision encoders with language decoders, trained on image-text pairs.",
        key_components=["Vision Encoder", "Embedding Projection", "Language Decoder", "Attention Module"],
        complexity_metrics=ComplexityMetrics(
            model_size="Vision: 100M-1B, Decoder: 1B-7B",
            time_complexity="O(image_tokens × seq_len)",
            space_complexity="~2-10GB",
            latency_target="p95 <500ms per image",
            throughput_target="100-500 img/s"
        )
    ),
    GenAISystem(
        number=10,
        title="Realistic Face Generation (GAN)",
        category="Multimodal Image",
        objective="Synthesizes photorealistic human faces using Generative Adversarial Networks, trained on face datasets to capture diverse identities and expressions.",
        key_components=["Generator Network", "Discriminator", "Latent Space", "Face Loss Functions"],
        complexity_metrics=ComplexityMetrics(
            model_size="500M-2B",
            time_complexity="O(1) inference (fixed forward pass)",
            space_complexity="~1-4GB",
            latency_target="p95 <100ms",
            throughput_target="100-1000 faces/s"
        )
    ),
    GenAISystem(
        number=11,
        title="High-Resolution Image Synthesis",
        category="Multimodal Image",
        objective="Generates high-quality images at 1024x1024+ resolution using diffusion models or multi-stage GANs, enabling detailed visual creation.",
        key_components=["Diffusion Model", "Scheduler", "Upsampling Stages", "Quality Refinement"],
        complexity_metrics=ComplexityMetrics(
            model_size="1B-5B",
            time_complexity="O(diffusion_steps × image_size²)",
            space_complexity="~4-20GB (multi-stage)",
            latency_target="p95 5-30s (quality dependent)",
            throughput_target="1-10 img/s per GPU"
        )
    ),
    GenAISystem(
        number=12,
        title="Text-to-Image Generation",
        category="Multimodal Image",
        objective="Converts text descriptions into images using diffusion models with text conditioning (CLIP + Diffusion), enabling creative visual synthesis.",
        key_components=["Text Encoder (CLIP)", "Diffusion Model", "Noise Scheduler", "Upsampler"],
        complexity_metrics=ComplexityMetrics(
            model_size="Text: 300M, Diffusion: 1B-5B",
            time_complexity="O(timesteps × image_size²)",
            space_complexity="~5-15GB",
            latency_target="p95 10-60s",
            throughput_target="1-5 img/s per GPU"
        )
    ),
    GenAISystem(
        number=13,
        title="Personalized Headshot Generation",
        category="Multimodal Image",
        objective="Generates professional headshots customized to user preferences by training adapter models on user-provided example images.",
        key_components=["Base Diffusion Model", "LoRA Adapters", "Style Embedding", "Quality Classifier"],
        complexity_metrics=ComplexityMetrics(
            model_size="Base: 1B, LoRA: 10-100M per user",
            time_complexity="O(diffusion_steps)",
            space_complexity="~1-2GB + per-user adapters",
            latency_target="p95 15-30s (generation + classification)",
            throughput_target="5-20 headshots/s with batching"
        )
    ),
    GenAISystem(
        number=14,
        title="Visual Question Answering",
        category="Multimodal Image",
        objective="Answers questions about image content by combining vision and language models, requiring both image understanding and reasoning.",
        key_components=["Vision Encoder", "Question Encoder", "Fusion Module", "Answer Decoder"],
        complexity_metrics=ComplexityMetrics(
            model_size="Vision: 100M-1B, Language: 1B-7B",
            time_complexity="O(visual_tokens × seq_len)",
            space_complexity="~2-10GB",
            latency_target="p95 <500ms per question",
            throughput_target="50-200 q/s"
        )
    ),
    GenAISystem(
        number=15,
        title="Product Photo Background Removal and Staging",
        category="Multimodal Image",
        objective="Removes product backgrounds and stages items in desired environments using segmentation and inpainting, enabling e-commerce automation.",
        key_components=["Segmentation Model", "Inpainting Model", "Background Generator", "Composition Engine"],
        complexity_metrics=ComplexityMetrics(
            model_size="Segmentation: 100M, Inpainting: 500M-1B",
            time_complexity="O(image_size²)",
            space_complexity="~1-3GB",
            latency_target="p95 <1s per product",
            throughput_target="100-500 products/s"
        )
    ),
    
    # Multimodal Video & Audio (3 systems)
    GenAISystem(
        number=16,
        title="Text-to-Video Generation",
        category="Multimodal Video & Audio",
        objective="Generates video sequences from text descriptions using diffusion models or autoregressive transformers, enabling creative video synthesis.",
        key_components=["Text Encoder", "Video Diffusion Model", "Frame Consistency Manager", "Upsampler"],
        complexity_metrics=ComplexityMetrics(
            model_size="3B-10B",
            time_complexity="O(num_frames × frame_resolution²)",
            space_complexity="~10-50GB",
            latency_target="p95 1-5 minutes per 10s clip",
            throughput_target="0.1-1 video/s per GPU"
        )
    ),
    GenAISystem(
        number=17,
        title="AI Video Subtitle and Dubbing System",
        category="Multimodal Video & Audio",
        objective="Automatically generates subtitles and dubbed audio in multiple languages for videos using speech recognition, translation, and text-to-speech.",
        key_components=["ASR Model", "Speech-to-Text", "Translation Engine", "TTS Model", "Lip-sync Alignment"],
        complexity_metrics=ComplexityMetrics(
            model_size="ASR: 500M-2B, TTS: 100M-1B per language",
            time_complexity="O(video_duration)",
            space_complexity="~3-10GB",
            latency_target="<1x video duration (real-time)",
            throughput_target="10-100 videos/day"
        )
    ),
    GenAISystem(
        number=18,
        title="Music Generation from Text Prompt",
        category="Multimodal Video & Audio",
        objective="Composes original music from text descriptions using diffusion models or autoregressive models trained on MIDI and audio datasets.",
        key_components=["Text Encoder", "Music Diffusion Model", "Vocoder", "Genre/Style Embedder"],
        complexity_metrics=ComplexityMetrics(
            model_size="1B-5B",
            time_complexity="O(duration × sample_rate)",
            space_complexity="~5-20GB",
            latency_target="p95 30s-5min per minute of music",
            throughput_target="0.1-1 track/s per GPU"
        )
    ),
    
    # Infrastructure & ML Systems (5 systems)
    GenAISystem(
        number=19,
        title="LLM Serving Infrastructure",
        category="Infrastructure",
        objective="Manages low-latency, high-throughput serving of large language models across distributed GPU clusters, handling batching, caching, and dynamic scaling.",
        key_components=["Request Router", "Batch Scheduler", "KV Cache Manager", "Load Balancer", "Monitoring"],
        complexity_metrics=ComplexityMetrics(
            model_size="Variable (7B-70B+)",
            time_complexity="O(batch_size × seq_len²)",
            space_complexity="~2x model size for activations",
            latency_target="p95 <1s per request",
            throughput_target="1000-10000 req/s per cluster"
        )
    ),
    GenAISystem(
        number=20,
        title="Online Fine-Tuning and RLHF Pipeline",
        category="Infrastructure",
        objective="Enables continuous model improvement through reinforcement learning from human feedback (RLHF), training reward models and updating base models online.",
        key_components=["Data Collection Pipeline", "Reward Model", "Policy Optimizer", "Evaluation Framework"],
        complexity_metrics=ComplexityMetrics(
            model_size="Base: 7B-70B, Reward: 1B-7B",
            time_complexity="O(iterations × batch_size × seq_len²)",
            space_complexity="~4-6x base model size",
            latency_target="N/A (batch training)",
            throughput_target="100-1000 training examples/day"
        )
    ),
    GenAISystem(
        number=21,
        title="ML Feature Store for GenAI",
        category="Infrastructure",
        objective="Manages feature engineering, storage, and retrieval for ML/GenAI systems, ensuring consistent features across training and serving.",
        key_components=["Feature Definition Registry", "Feature Computation Engine", "Vector DB", "Cache Layer"],
        complexity_metrics=ComplexityMetrics(
            model_size="N/A (data storage system)",
            time_complexity="O(log n) for retrieval",
            space_complexity="~1-100GB per feature set",
            latency_target="p95 <100ms for feature retrieval",
            throughput_target="10k-100k feature lookups/s"
        )
    ),
    GenAISystem(
        number=22,
        title="Evaluation and Red-Teaming Platform",
        category="Infrastructure",
        objective="Systematically evaluates GenAI models for quality, safety, and bias through automated benchmarks, human evaluation, and adversarial testing.",
        key_components=["Benchmark Suite", "Evaluation Metrics Engine", "Red-team Prompt Generator", "Result Aggregator"],
        complexity_metrics=ComplexityMetrics(
            model_size="Varies per evaluation",
            time_complexity="O(num_evaluations × test_size)",
            space_complexity="~10-100GB results storage",
            latency_target="N/A (batch evaluation)",
            throughput_target="1000-10000 evaluations/day"
        )
    ),
]


def get_all_systems():
    """Return all 22 GenAI systems."""
    return ALL_SYSTEMS


def get_systems_by_category(category: str):
    """Get systems filtered by category."""
    return [s for s in ALL_SYSTEMS if s.category == category]


def validate_systems_data():
    """Validate systems data integrity."""
    assert len(ALL_SYSTEMS) == 21, f"Expected 21 systems, got {len(ALL_SYSTEMS)}"
    
    # Check numbering
    expected_numbers = list(range(2, 23))
    actual_numbers = sorted([s.number for s in ALL_SYSTEMS])
    assert actual_numbers == expected_numbers, f"System numbers mismatch"
    
    # Check categories
    categories = {}
    for system in ALL_SYSTEMS:
        if system.category not in categories:
            categories[system.category] = []
        categories[system.category].append(system)
    
    expected_counts = {
        'Foundations': 2,
        'Language & Dialogue': 5,
        'Multimodal Image': 7,
        'Multimodal Video & Audio': 3,
        'Infrastructure': 4
    }
    
    for category, count in expected_counts.items():
        actual_count = len(categories.get(category, []))
        assert actual_count == count, f"{category}: expected {count}, got {actual_count}"
    
    print("✓ Systems data validation passed")
