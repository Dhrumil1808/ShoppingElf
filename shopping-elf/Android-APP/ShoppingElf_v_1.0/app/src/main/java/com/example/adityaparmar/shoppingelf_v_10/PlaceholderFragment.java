package com.example.adityaparmar.shoppingelf_v_10;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.example.adityaparmar.shoppingelf_v_10.adapter.MyCardsAdapter;
import com.example.adityaparmar.shoppingelf_v_10.model.MyCards;
import com.example.adityaparmar.shoppingelf_v_10.service.CardsClient;

import java.util.List;

import okhttp3.OkHttpClient;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

/**
 * Created by adityaparmar on 5/7/17.
 */

public  class PlaceholderFragment extends Fragment {



    private static final String ARG_SECTION_NUMBER = "section_number";
    private List<MyCards> glist;
    RecyclerView rv;

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
                rv = (RecyclerView) rootView.findViewById(R.id.rc_grocery_card);
                rv.setHasFixedSize(true);



                feedData();



                LinearLayoutManager llm = new LinearLayoutManager(getActivity());
                rv.setLayoutManager(llm);
                break;
            }
            case 3:
            {
                rootView = inflater.inflate(R.layout.fragment_graph, container, false);

                break;
            }
            case 4:{

                rootView = inflater.inflate(R.layout.fragment_notification, container, false);
                break;

            }



        }
        return rootView;
    }





    public void feedData()
    {
        String API_BASE_URL = "http://54.241.140.236:3008/";

        OkHttpClient.Builder httpClient = new OkHttpClient.Builder();

        Retrofit.Builder builder = new Retrofit.Builder()
                .baseUrl(API_BASE_URL)
                .addConverterFactory(
                        GsonConverterFactory.create()
                );

        Retrofit retrofit = builder.client(httpClient.build()).build();



        CardsClient client =  retrofit.create(CardsClient.class);

        // Fetch a list of the Github repositories.
        Call<List<MyCards>> call = client.getcards();

        // Execute the call asynchronously. Get a positive or negative callback.
        call.enqueue(new Callback<List<MyCards>>() {
            @Override
            public void onResponse(Call<List<MyCards>> call, Response<List<MyCards>> response) {
                // The network call was a success and we got a response
                // TODO: use the repository list and display it
                glist = response.body();
                MyCardsAdapter adapter = new MyCardsAdapter(glist);
                rv.setAdapter(adapter);

                //Toast.makeText(getActivity(),response.body().get(1).getProductName(),Toast.LENGTH_LONG).show();
               //listView.setAdapter(new GitHubRepoAdapter(Recto.this,respo));
               // Toast.makeText(Recto.this,"positive responce", Toast.LENGTH_LONG);
            }

            @Override
            public void onFailure(Call<List<MyCards>> call, Throwable t) {
                // the network call was a failure
                // TODO: handle error
            }
        });
    }


}