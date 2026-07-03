"use client";

import { useState } from "react";
import { generateAiContent } from "@/lib/api";
import type { GeneratedContent } from "@/lib/types";

type AiGeneratorProps = {
  productId: number;
};

export function AiGenerator({ productId }: AiGeneratorProps) {
  const [content, setContent] = useState<GeneratedContent | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleGenerate() {
    setIsLoading(true);
    setError(null);

    try {
      const result = await generateAiContent(productId);
      setContent(result);
    } catch {
      setError("AI content could not be generated. Make sure the backend is running.");
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <section className="panel">
      <p className="eyebrow">AI Studio</p>
      <h2 className="product-title">Generate product content</h2>
      <p className="description">
        Create mock launch copy, a tagline, and a social caption for this product.
      </p>
      <button className="button" type="button" onClick={handleGenerate} disabled={isLoading}>
        {isLoading ? "Generating..." : "Generate AI content"}
      </button>

      {error ? <p className="description">{error}</p> : null}

      {content ? (
        <div className="ai-output">
          <h3>{content.title}</h3>
          <p>
            <strong>Tagline:</strong> {content.tagline}
          </p>
          <p>{content.description}</p>
          <p>
            <strong>Social:</strong> {content.social_caption}
          </p>
        </div>
      ) : null}
    </section>
  );
}

