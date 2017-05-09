package com.example.adityaparmar.shoppingelf_v_10.adapter;

/**
 * Created by adityaparmar on 5/7/17.
 */

import android.support.v7.widget.CardView;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.example.adityaparmar.shoppingelf_v_10.R;
import com.example.adityaparmar.shoppingelf_v_10.model.MyModel;

import java.util.List;

public class MyAdapter extends RecyclerView.Adapter<MyAdapter.MyViewHolder> {
    //private String[] mDataset;
    private List<MyModel> mDataset;

    // Provide a reference to the views for each data item
    // Complex data items may need more than one view per item, and
    // you provide access to all the views for a data item in a view holder
    public static class MyViewHolder extends RecyclerView.ViewHolder {
        public CardView mCardView;
        public TextView tv_Date;
        public TextView tv_Items;
        public TextView tv_Status;
        public TextView tv_Message;

        public MyViewHolder(View v) {
            super(v);

            mCardView = (CardView) v.findViewById(R.id.card_view);
            tv_Date = (TextView) v.findViewById(R.id.tv_Date);
            tv_Items = (TextView)v.findViewById(R.id.tv_items);
            tv_Status = (TextView)v.findViewById(R.id.tv_status);
            tv_Message = (TextView) v.findViewById(R.id.tv_message);

        }
    }

    // Provide a suitable constructor (depends on the kind of dataset)
    public MyAdapter(List<MyModel>  myDataset) {
        mDataset = myDataset;
    }

    // Create new views (invoked by the layout manager)
    @Override
    public MyAdapter.MyViewHolder onCreateViewHolder(ViewGroup parent,
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
        MyModel members = mDataset.get(position);

        holder.tv_Date.setText("Date: "+members.getDate());
        holder.tv_Items.setText("Items: "+Integer.toString(members.getItems()));
        holder.tv_Status.setText("Status: "+ members.getStatus());
        holder.tv_Message.setText("Message:"+members.getMessage());

    }

    @Override
    public int getItemCount() {
        return mDataset.size();
    }
}