import streamlit as st
import pandas as pd

# Function to upload Excel files and select columns
def upload_and_select_columns():
    uploaded_files = st.file_uploader("Upload Excel files", accept_multiple_files=True, type=["xlsx", "xls"])
    selected_columns = []

    if uploaded_files:
        for file in uploaded_files:
            st.write(f"### {file.name}")
            df = pd.read_excel(file)

            # Display dataframe for column selection
            selected_columns.append(st.multiselect(f"Select columns from {file.name}", df.columns.tolist()))

    return uploaded_files, selected_columns

# Function to merge selected columns
def merge_columns(files, selected_columns):
    merged_df = pd.DataFrame()

    for i, file in enumerate(files):
        df = pd.read_excel(file)
        selected_cols = selected_columns[i]
        merged_df = pd.concat([merged_df, df[selected_cols]], axis=1)

    return merged_df

def main():
    st.title("Excel Column Selector")

    # Upload files and select columns
    files, selected_cols = upload_and_select_columns()

    # Merge selected columns
    if st.button("Merge Columns"):
        merged_df = merge_columns(files, selected_cols)
        st.write("### Merged Data")
        st.write(merged_df)

        # Download merged data
        csv = merged_df.to_csv(index=False)
        st.download_button(
            label="Download Merged Data",
            data=csv,
            file_name="merged_data.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()
