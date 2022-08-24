import { SlowBuffer } from "buffer";
import React from "react";
import "../App.css";
import { useAppSelector, useAppDispatch } from "../App/hooks";

const Product = (props: any): JSX.Element => {
  const orders = useAppSelector((state) => state);
  const dispatch = useAppDispatch();
  return (
    <div className="product-card">
      <h3>{props.product.description}</h3>
      <h4>{props.product.price}</h4>
      <button
        value={props.product.price}
        name={props.product.description}
        onClick={() => {
          dispatch({ type: "ADD_TO_CART", payload: props.product });
        }}
      >
        Add to Cart
      </button>
    </div>
  );
};

export default Product;
