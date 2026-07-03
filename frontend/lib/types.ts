export type Product = {
  id: number;
  name: string;
  description: string;
  price: number;
  image_url: string;
  tags: string[];
  rating: number;
};

export type GeneratedContent = {
  product_id: number;
  title: string;
  tagline: string;
  description: string;
  social_caption: string;
};

