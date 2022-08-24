import React from "react";
import { useAppSelector, useAppDispatch } from "../App/hooks";
import "../App.css";

const CartItem = (props: any) => {
  const dispatch = useAppDispatch();
  return (
    <div className="cart-card">
      <h3>{props.item.description}</h3>
      <h4>{props.item.price}</h4>
    </div>
  );
};

export default CartItem;
