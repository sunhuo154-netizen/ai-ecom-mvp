import { ProductCard } from "@/components/ProductCard";
import { getHotProducts } from "@/lib/api";

export default async function HomePage() {
  const products = await getHotProducts();

  return (
    <main className="page">
      <header className="header">
        <div>
          <p className="eyebrow">AI E-commerce MVP</p>
          <h1>Hot products ready for AI-powered selling.</h1>
          <p className="subtitle">
            Browse mock products from the FastAPI backend and generate marketing content on each product page.
          </p>
        </div>
      </header>

      <section className="product-grid">
        {products.map((product) => (
          <ProductCard product={product} key={product.id} />
        ))}
      </section>
    </main>
  );
}

