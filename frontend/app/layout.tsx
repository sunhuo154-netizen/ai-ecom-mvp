import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI E-commerce MVP",
  description: "Mock AI e-commerce product discovery app"
};

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

