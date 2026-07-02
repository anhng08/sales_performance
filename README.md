# Sales Performance Analysis

## Overview
This project looks at a company's sales data from 2014 to 2018 to answer a simple business question: **"How is our sales performance doing, and where is the money coming from?"**

I took raw sales and marketing data, cleaned and organized it, then built visual reports to help decision-makers quickly understand revenue trends, top customers, best-selling products, and how well marketing campaigns are working.

## 1. Specific Problems
- Marketing spent 15.3M, but **there's no way to tell which campaign actually drove revenue**, since multiple campaigns ran during overlapping periods
- Revenue is **concentrated in a small group of products** (Product 26, 25, 13...) — risky if demand for that group shifts, but the actual level of risk hasn't been measured
- There's no campaign ID or link connecting **a customer's order to the campaign that reached them**, so ROI per campaign can't be calculated

## 2. Business Questions
1. **Campaign efficiency**: Among the 10 campaigns, which has the best and worst cost-to-revenue ratio, and should budget be cut from the underperforming ones?
2. **Product concentration risk**: What % of total revenue currently depends on the top 5 products, and how much would total revenue drop if demand for one of those products fell?
3. **Recommendation**: Where should campaign ID / UTM tracking be implemented first (checkout, landing page, or CRM) so the next reporting period can accurately measure marketing ROI?

## 🎯 What This Project Covers
- **Sales Performance:** Revenue and profit trends over 5 years
- **Customer & Product Analysis:** Which customers and products drive the most revenue
- **Sales Channels & Regions:** Where the business is strongest (and weakest)
- **Marketing Campaigns:** How effective marketing spend has been at driving sales
- **Data Limitations:** An honest look at what the data *can't* tell us yet
- **Recommendations:** Concrete next steps to fix data gaps and improve tracking

## 🛠️ How It Was Built
| Step | Tool Used |
|------|-----------|
| Data cleaning & column mapping | Python |
| Loading & organizing data | SQL |
| Dashboard & visual reporting | Power BI |

## 📈 Key Findings
- **Total revenue:** 205.99M | **Total profit:** 190.69M | **Total orders:** 11K
- The **Wholesale channel** drives the majority of revenue (~54%), followed by Distributor (~31%) and Export (~15%).
- Revenue is **geographically balanced**, with the West region slightly ahead.
- No single customer dominates revenue — the customer base is well diversified.
- A small group of products generates a large share of revenue, which is good for focus but risky if demand for those products shifts.

## ⚠️ Data Limitations
Marketing campaigns have cost data, but **we currently can't prove which campaign generated which sale**, because:
- Multiple campaigns often run at the same time (overlapping periods)
- Customer purchases aren't linked to specific campaigns
- Key details like campaign channel, target audience, and platform are missing from the data

## 💡 Recommendations
1. Give every marketing campaign a unique tracking ID
2. Connect marketing data with sales/customer data in one central place
3. Add UTM tracking links to campaigns
