package com.example.adityaparmar.shoppingelf_v_10.adapter;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import com.example.adityaparmar.shoppingelf_v_10.R;
import com.example.adityaparmar.shoppingelf_v_10.model.GitHubRepo;

import java.util.List;

/**
 * Created by adityaparmar on 5/8/17.
 */

public class GitHubRepoAdapter extends ArrayAdapter<GitHubRepo> {

private Context context;
private List<GitHubRepo> values;

public GitHubRepoAdapter(Context context, List<GitHubRepo> values) {
        super(context, R.layout.activity_recto, values);

        this.context = context;
        this.values = values;
        }

@Override
public View getView(int position, View convertView, ViewGroup parent) {
        View row = convertView;

        if (row == null) {
        LayoutInflater inflater =
        (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        row = inflater.inflate(R.layout.activity_recto_content, parent, false);
        }

        TextView textView = (TextView) row.findViewById(R.id.txtlistitems);

        GitHubRepo item = values.get(position);
        String message = item.getProductName();
        textView.setText(message);

        return row;
        }
        }
