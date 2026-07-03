import type { GeneratedContent, Product } from "./types";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

export async function getHotProducts(): Promise<Product[]> {
  const response = await fetch(`${API_BASE_URL}/api/products/hot`, {
    next: { revalidate: 30 }
  });

  if (!response.ok) {
    throw new Error("Failed to load products");
  }

  return response.json();
}

export async function getProduct(id: string): Promise<Product> {
  const products = await getHotProducts();
  const product = products.find((item) => item.id === Number(id));

  if (!product) {
    throw new Error("Product not found");
  }

  return product;
}

export async function generateAiContent(productId: number): Promise<GeneratedContent> {
  const response = await fetch(`${API_BASE_URL}/api/ai/generate`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      product_id: productId,
      tone: "friendly"
    })
  });

  if (!response.ok) {
    throw new Error("Failed to generate content");
  }

  return response.json();
}
