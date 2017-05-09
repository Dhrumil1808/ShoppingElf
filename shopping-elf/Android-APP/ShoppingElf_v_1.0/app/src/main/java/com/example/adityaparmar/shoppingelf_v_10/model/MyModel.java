package com.example.adityaparmar.shoppingelf_v_10.model;

/**
 * Created by adityaparmar on 5/7/17.
 */

public class MyModel {

    String Date;
    int Items;
    String Status;
    String Message;

    public MyModel( int items,String date, String status, String message) {
        Date = date;
        Items = items;
        Status = status;
        Message = message;
    }

    public String getDate() {
        return Date;
    }

    public int getItems() {
        return Items;
    }

    public String getStatus() {
        return Status;
    }

    public String getMessage() {
        return Message;
    }
    public void setDate(String date) {
        Date = date;
    }

    public void setItems(int items) {
        Items = items;
    }

    public void setStatus(String status) {
        Status = status;
    }

    public void setMessage(String message) {
        Message = message;
    }

}
