import Link from "next/link";
import { AiGenerator } from "@/components/AiGenerator";
import { getProduct } from "@/lib/api";

type ProductPageProps = {
  params: {
    id: string;
  };
};

export default async function ProductPage({ params }: ProductPageProps) {
  const product = await getProduct(params.id);

  return (
    <main className="page">
      <Link className="button secondary" href="/">
        Back to products
      </Link>

      <section className="detail-layout" style={{ marginTop: 24 }}>
        <img className="detail-image" src={product.image_url} alt={product.name} />

        <div className="panel">
          <p className="eyebrow">Rated {product.rating}/5</p>
          <h1>{product.name}</h1>
          <p className="subtitle">{product.description}</p>
          <p className="price" style={{ fontSize: "1.5rem" }}>
            ${product.price.toFixed(2)}
          </p>
          <div className="tags">
            {product.tags.map((tag) => (
              <span className="tag" key={tag}>
                {tag}
              </span>
            ))}
          </div>
        </div>

        <AiGenerator productId={product.id} />
      </section>
    </main>
  );
}

