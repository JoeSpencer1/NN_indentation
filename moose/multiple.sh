#!/bin/bash

# Path to the input file
REF='3'
REFI='0'
DIM='2'
ORDER='l'
COUNT=0

INPUT_FILE="properties.csv"

# Create outputs directory if it doesn't exist
mkdir -p outputs

# Debug: Count total lines in the file excluding the header
TOTAL_LINES=$(($(wc -l < "$INPUT_FILE")))
echo "Total lines (excluding header): $TOTAL_LINES"

# Loop through the expected number of lines (25)
for (( i=1; i<=TOTAL_LINES; i++ )); do
    # Read the specific line from the CSV file
    IFS=',' read -ra row <<< "$(sed -n "$((i+1))p" "$INPUT_FILE")"

    # Check if the row is empty or only contains whitespace
    if [[ -z "${row[*]}" || "${#row[@]}" -eq 0 ]]; then
        echo "Warning: Empty row, skipping."
        continue
    fi

    echo "Processing row: ${row[@]}"
    
    # Ensure there are enough columns in the row
    if [[ ${#row[@]} -lt 7 ]]; then
        echo "Warning: Not enough columns in the row, skipping."
        continue
    fi
    
    # Assign values to variables based on the provided column layout
    E="${row[0]}"
    sy="${row[1]}"
    nu="${row[2]}"
    n="${row[3]}"
    hm="${row[4]}"
    K="${row[6]}"

    # Remove any leading/trailing whitespace
    E=$(echo "$E" | xargs)
    sy=$(echo "$sy" | xargs)
    nu=$(echo "$nu" | xargs)
    n=$(echo "$n" | xargs)
    hm=$(echo "$hm" | xargs)
    K=$(echo "$K" | xargs)

    echo "Parameters: E=$E, sy=$sy, nu=$nu, n=$n, hm=$hm, K=$K"

    # Execute the MPI command with the current set of parameters
    mpiexec -n 4 ~/projects/moose/modules/contact/contact-opt -i ind_${DIM}D.i \
    -input-params ref=$REF refi=$REFI E=$E K=$K n=$n hm=$hm
    
    # Check if the output file exists
    if [ -f "ind_${DIM}D_out.csv" ]; then
        # Move the output file to the outputs directory with the correct count
        mv "ind_${DIM}D_out.csv" "outputs/data_FEM/ind_${DIM}D_${REF}${ORDER}/ind_${DIM}D_${REF}${ORDER}_${COUNT}_out.csv"
        echo "Moved output file to outputs/data_FEM/ind_${DIM}D_${REF}${ORDER}/ind_${DIM}D_${REF}${ORDER}_${COUNT}_out.csv"
    else
        echo "Warning: Output file ind_${DIM}D_out.csv not found"
    fi
    
    # Increment the count
    COUNT=$((COUNT + 1))
    
    echo "Completed iteration $COUNT"
    echo "------------------------"
    
    # Optional: Add a delay between runs or any other desired actions
    sleep 1
done

echo "Total iterations: $COUNT"
