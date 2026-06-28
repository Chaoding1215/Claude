---
name: ian-xiaolei-illustrations
version: "1.0.0"
description: "Generate and manage illustrations in the style of Ian Xiaolei - clean, minimal line art with expressive characters and soft color palettes."
argument-hint: 'ian-xiaolei-illustrations character sketch | ian-xiaolei-illustrations scene composition | ian-xiaolei-illustrations color palette'
user-invocable: true
author: chaoding1215
license: MIT
---

# Ian Xiaolei Illustrations Skill

This skill helps you create, manage, and iterate on illustrations inspired by Ian Xiaolei's distinctive visual style: clean minimal line art, expressive characters, soft muted color palettes, and thoughtful compositions.

## Style Reference

Ian Xiaolei's illustration style is characterized by:

- **Line art**: Clean, confident strokes with minimal detail — every line serves a purpose
- **Characters**: Expressive faces with simple features; emotions conveyed through posture and gesture
- **Color palette**: Soft, muted tones — dusty pinks, sage greens, warm creams, slate blues
- **Composition**: Generous negative space; subjects placed intentionally within the frame
- **Mood**: Quiet, introspective, often solitary figures in everyday moments

## How to Use

Invoke this skill with a subject or scene to get:

1. A detailed illustration brief (style notes, composition, palette)
2. A ready-to-use prompt for AI image generation tools (Midjourney, DALL-E, Stable Diffusion)
3. Optional: color hex codes matching the described palette

## Invocation Examples

- `/ian-xiaolei-illustrations a person reading by a window`
- `/ian-xiaolei-illustrations two friends sharing an umbrella in the rain`
- `/ian-xiaolei-illustrations a cat on a rooftop at dusk`

## Output Format

For each request, produce:

### Illustration Brief
A short paragraph describing the scene, mood, and composition in Ian Xiaolei's style.

### AI Image Prompt
A ready-to-copy prompt optimized for image generation. Always include:
- Style anchors: `clean line art`, `minimal illustration`, `soft color palette`, `expressive characters`
- Mood anchors relevant to the scene
- Negative prompts: `no heavy shading`, `no photorealism`, `no complex backgrounds`

### Color Palette
3–5 hex codes with names that match the scene's mood.

## Iteration

After delivering the first result, ask:
> "Want me to adjust the composition, shift the palette, or try a different mood?"

Stay in the skill context until the user is satisfied or explicitly exits.
