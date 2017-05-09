package com.example.adityaparmar.shoppingelf_v_10;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.example.adityaparmar.shoppingelf_v_10.model.MyModel;

import java.util.ArrayList;
import java.util.List;

import com.example.adityaparmar.shoppingelf_v_10.adapter.MyAdapter;

/**
 * Created by adityaparmar on 5/7/17.
 */

public  class PlaceholderFragment extends Fragment {



    private static final String ARG_SECTION_NUMBER = "section_number";

    public PlaceholderFragment() {
    }


    public static PlaceholderFragment newInstance(int sectionNumber) {
        PlaceholderFragment fragment = new PlaceholderFragment();
        Bundle args = new Bundle();
        args.putInt(ARG_SECTION_NUMBER, sectionNumber);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_receipt, container, false);

        // TextView textView = (TextView) rootView.findViewById(R.id.section_label);


        switch (getArguments().getInt(ARG_SECTION_NUMBER))
        {
            case 1: {
                rootView = inflater.inflate(R.layout.fragment_receipt, container, false);



                break;
            }
            case 2: {
                rootView = inflater.inflate(R.layout.fragment_shopping_card, container, false);
                RecyclerView rv = (RecyclerView) rootView.findViewById(R.id.rc_grocery_card);
                rv.setHasFixedSize(true);
                   /* MyModel[] data = new MyModel[2];
                    data[0].setItems("I am first");
                    data[1].setItems("I am first");
                    */
                List<MyModel> list = new ArrayList<>();
                MyModel data;
                for(int i=0;i<5;i++)
                {
                    data = new MyModel(
                            i,"hello","hello","hello"

                    );
                    list.add(data);
                }



                MyAdapter adapter = new MyAdapter(list);

                rv.setAdapter(adapter);

                LinearLayoutManager llm = new LinearLayoutManager(getActivity());
                rv.setLayoutManager(llm);
                break;
            }


        }
        return rootView;
    }


}