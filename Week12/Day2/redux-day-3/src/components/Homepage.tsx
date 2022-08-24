import React from "react";
import Cart from "./Cart";
import Product from "./Product";
import "../App.css";
import { useAppSelector, useAppDispatch } from "../App/hooks";
import CartItem from "./CartItem";
import { createClient } from "@supabase/supabase-js";

const Homepage = (): JSX.Element => {
  // const counter = useAppSelector((state) => state.counter);
  const products = useAppSelector((state) => state.products);
  const cartItems = useAppSelector((state) => state.cart);
  const dispatch = useAppDispatch();
  const supabaseUrl = "https://mxakcphctxajogkuteth.supabase.co";
  const supabaseAnonKey =
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYyMDE0NTg3OCwiZXhwIjoxOTM1NzIxODc4fQ.0qra9FQYuKCkgMteZ0ZAe2wrMx2v1IFGwsU60Oi4KwY";
  const supabase = createClient(supabaseUrl, supabaseAnonKey);
  const sendToDatabase = async () => {
    const { data, error } = await supabase
      .from("ProductsDatabase")
      .insert([{ name: "Blake", items: cartItems }]);
  };

  return (
    <div>
      <h1>Home Page</h1>
      <div className="homepage">
        <div className="product-container">
          <h1>Products will go here</h1>
          {products.map((product) => (
            <Product product={product} />
          ))}
        </div>
        <div className="cart-container">
          <h1>Cart Items will go here</h1>
          {cartItems.map((item) => (
            <CartItem item={item} />
          ))}
          <button className="check-out" onClick={() => sendToDatabase()}>
            Check Out
          </button>
        </div>
      </div>
    </div>
  );
};

export default Homepage;
