package com.example.adityaparmar.shoppingelf_v_10.adapter;

import android.support.v7.widget.CardView;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import com.example.adityaparmar.shoppingelf_v_10.R;
import com.example.adityaparmar.shoppingelf_v_10.model.MyCards;

import java.util.List;
import java.util.Random;

/**
 * Created by adityaparmar on 5/8/17.
 */

public class MyCardsAdapter extends RecyclerView.Adapter<MyCardsAdapter.MyViewHolder>  {
    //private String[] mDataset;
    private List<MyCards> mDataset;

    // Provide a reference to the views for each data item
    // Complex data items may need more than one view per item, and
    // you provide access to all the views for a data item in a view holder
    public static class MyViewHolder extends RecyclerView.ViewHolder {
        public CardView mCardView;
        public TextView tv_product;
        public TextView tv_quanty;
        public TextView tv_remainingdays;
        public TextView tv_lastpurchase;
        public ImageView imageView;
        public View view;

        public MyViewHolder(View v) {
            super(v);

            mCardView = (CardView) v.findViewById(R.id.card_view);
            tv_product = (TextView) v.findViewById(R.id.tv_Product);
            tv_remainingdays = (TextView)v.findViewById(R.id.tv_daysRemaining);
            //tv_quanty = (TextView)v.findViewById(R.id.tv_Quantity);
            tv_lastpurchase = (TextView)v.findViewById(R.id.tv_lastbuy);
            imageView = (ImageView)v.findViewById(R.id.iv_image);
            view = (View)v.findViewById(R.id.stockstatus);


        }
    }

    // Provide a suitable constructor (depends on the kind of dataset)
    public MyCardsAdapter(List<MyCards>  myDataset) {
        mDataset = myDataset;
    }

    // Create new views (invoked by the layout manager)
    @Override
    public MyCardsAdapter.MyViewHolder onCreateViewHolder(ViewGroup parent,
                                                     int viewType) {
        // create a new view
        View v = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.gc_cards, parent, false);
        // set the view's size, margins, paddings and layout parameters
        MyViewHolder vh = new MyViewHolder(v);
        return vh;
    }

    @Override
    public void onBindViewHolder(MyViewHolder holder, int position) {
        MyCards members = mDataset.get(position);



            holder.tv_product.setText("Product: " + members.getProductName().toUpperCase());

            holder.tv_lastpurchase.setText("Last bought on : " + members.getLastBilldate());

            //holder.tv_quanty.setText("Quantity: " + Integer.toString(members.getQuantity()));


            holder.tv_remainingdays.setText(members.getProductName().toUpperCase()+" will be out of stock in "+members.getEstimated_days_to_last()+" days.");

            if(members.getEstimated_days_to_last() >= 5)
            {
                Random rand = new Random();
                int  n1 = rand.nextInt(3) + 1;
                if(n1 == 1){

                    holder.imageView.setImageResource(R.drawable.fullstock);
                }
                else if(n1 == 2){

                    holder.imageView.setImageResource(R.drawable.fullstock2);
                }
                else{

                    holder.imageView.setImageResource(R.drawable.fullstock3);
                }

                holder.view.setBackgroundResource(R.color.stockfull);

            }
            else if(members.getEstimated_days_to_last() <= 2)
            {
                holder.view.setBackgroundResource(R.color.stockdanger);
                holder.imageView.setImageResource(R.drawable.fullstock3);
            }
            else
            {
                holder.view.setBackgroundResource(R.color.stocklimited);
                holder.imageView.setImageResource(R.drawable.fullstock);
            }





    }

    @Override
    public int getItemCount() {
        return mDataset.size();
    }
}
