# plots.py
import matplotlib.pyplot as plt
import numpy as np


def plot_city_attrition(city_summary):
    """Generates and saves the City Attrition Bar Chart in its own window."""
    plt.figure()  # CRITICAL: Opens a brand-new separate window frame

    plt.bar(
        city_summary["City"],
        city_summary["Attrition_Status"],
        color="#009688",
        edgecolor="black",
        width=0.6,
    )
    plt.title(
        "Employee Attrition Rate by City Location", fontsize=14, fontweight="bold"
    )
    plt.xlabel("City Branch", fontsize=12)
    plt.ylabel("Attrition Rate (Proportion)", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.axhline(y=0.35, color="red", linestyle=":", label="Company Avg (~35%)")
    plt.legend()
    plt.tight_layout()

    plt.savefig("1_attrition_by_city.png")
    plt.show(block=False)  # Display without freezing


def plot_intersection_attrition(gender_tier_summary):
    """Generates and saves the Payment Tier vs Gender Intersection Chart in its own window."""
    plt.figure()  # CRITICAL: Opens a brand-new separate window frame

    female_data = gender_tier_summary[gender_tier_summary["Gender"] == "Female"]
    male_data = gender_tier_summary[gender_tier_summary["Gender"] == "Male"]

    x_indices = np.arange(len(female_data["PaymentTier"]))
    bar_width = 0.35

    plt.bar(
        x_indices - bar_width / 2,
        female_data["Attrition_Status"],
        width=bar_width,
        label="Female",
        color="#ec407a",
        edgecolor="black",
    )
    plt.bar(
        x_indices + bar_width / 2,
        male_data["Attrition_Status"],
        width=bar_width,
        label="Male",
        color="#1e88e5",
        edgecolor="black",
    )

    plt.xticks(x_indices, female_data["PaymentTier"].astype(str))
    plt.title(
        "Attrition Trends: Payment Tier vs Gender Intersection",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Payment Tier (1 = Highest, 3 = Lowest)", fontsize=12)
    plt.ylabel("Attrition Rate (Proportion)", fontsize=12)
    plt.legend(title="Gender")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()

    plt.savefig("2_attrition_gender_payment_intersection.png")
    plt.show(block=False)  # Display without freezing


def plot_year_attrition(year_details):
    """Generates and saves the Dual-Axis Joining Year Chart."""
    # This one is already correct because 'plt.subplots()' naturally creates a new window!
    fig, ax1 = plt.subplots(figsize=(8, 5))
    years_str = year_details["JoiningYear"].astype(str)

    ax1.bar(
        years_str,
        year_details["count"],
        color="#e0e0e0",
        edgecolor="darkgrey",
        alpha=0.7,
        label="Intake Size",
    )
    ax1.set_xlabel("Hiring Cohort (Joining Year)", fontsize=12)
    ax1.set_ylabel("Total Employees Hired (Count)", color="grey", fontsize=12)
    ax1.tick_params(axis="y", labelcolor="grey")

    ax2 = ax1.twinx()
    ax2.plot(
        years_str,
        year_details["mean"],
        color="#d32f2f",
        marker="o",
        linewidth=2.5,
        label="Attrition Rate",
    )
    ax2.set_ylabel("Attrition Rate (Proportion)", color="#d32f2f", fontsize=12)
    ax2.tick_params(axis="y", labelcolor="#d32f2f")

    plt.title(
        "Workforce Attrition vs. Initial Intake Size by Year",
        fontsize=14,
        fontweight="bold",
    )
    plt.tight_layout()

    plt.savefig("3_attrition_vs_intake_by_year.png")
    plt.show(block=False)  # Display without freezing


def plot_overall_distribution(proportions):
    """Generates and saves the Overall Distribution Pie Chart in its own window."""
    plt.figure()  # CRITICAL: Opens a brand-new separate window frame

    labels = ["Stayed (0)", "Left (1)"]
    slice_colors = ["#4caf50", "#ff5722"]

    plt.pie(
        proportions,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
        colors=slice_colors,
        explode=(0, 0.05),
    )
    plt.title(
        "Overall Corporate Attrition Distribution", fontsize=14, fontweight="bold"
    )
    plt.tight_layout()

    plt.savefig("4_overall_attrition_distribution_pie.png")
    plt.show(block=False)  # Display without freezing
