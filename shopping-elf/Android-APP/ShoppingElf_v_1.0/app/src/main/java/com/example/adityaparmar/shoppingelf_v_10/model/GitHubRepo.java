package com.example.adityaparmar.shoppingelf_v_10.model;

/**
 * Created by adityaparmar on 5/8/17.
 */

public class GitHubRepo {

    public int getEstimate_days() {
        return estimate_days;
    }

    public void setEstimate_days(int estimate_days) {
        this.estimate_days = estimate_days;
    }

    public int getEstimated_days_to_last() {
        return estimated_days_to_last;
    }

    public void setEstimated_days_to_last(int estimated_days_to_last) {
        this.estimated_days_to_last = estimated_days_to_last;
    }

    public String getLastBilldate() {
        return lastBilldate;
    }

    public void setLastBilldate(String lastBilldate) {
        this.lastBilldate = lastBilldate;
    }

    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public GitHubRepo(int estimate_days, int estimated_days_to_last, String lastBilldate, String productName, int quantity) {
        this.estimate_days = estimate_days;
        this.estimated_days_to_last = estimated_days_to_last;
        this.lastBilldate = lastBilldate;
        this.productName = productName;
        this.quantity = quantity;
    }

    private int estimate_days;
    private int estimated_days_to_last;
    private String lastBilldate;
    private String productName;
    private int quantity;


}
