import Link from "next/link";
import type { Product } from "@/lib/types";

type ProductCardProps = {
  product: Product;
};

export function ProductCard({ product }: ProductCardProps) {
  return (
    <article className="product-card">
      <img className="product-image" src={product.image_url} alt={product.name} />
      <div className="product-body">
        <div className="product-title-row">
          <h2 className="product-title">{product.name}</h2>
          <span className="price">${product.price.toFixed(2)}</span>
        </div>
        <p className="description">{product.description}</p>
        <div className="tags">
          {product.tags.map((tag) => (
            <span className="tag" key={tag}>
              {tag}
            </span>
          ))}
        </div>
        <Link className="button" href={`/products/${product.id}`}>
          View product
        </Link>
      </div>
    </article>
  );
}

