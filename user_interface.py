def display_results(optimized_code):
    if not optimized_code:
        print("No optimizations were applied.")
    else:
        print("Optimizations applied:")
        for filename, optimization_result in optimized_code.items():
            if optimization_result["success"]:
                print(f"- {filename}: Optimized code written to {optimization_result['new_filename']}")
            else:
                print(f"- {filename}: Optimization failed due to {optimization_result['error_message']}")
