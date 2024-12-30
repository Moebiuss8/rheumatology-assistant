def calculate_posttest_probability(pretest_prob, sensitivity, specificity, test_result):
    """Calculate post-test probability using Bayes' theorem.
    
    Args:
        pretest_prob (float): Pre-test probability (0-1)
        sensitivity (float): Test sensitivity (0-1)
        specificity (float): Test specificity (0-1)
        test_result (bool): True for positive test, False for negative
    
    Returns:
        float: Post-test probability (0-1)
    """
    if not (0 <= pretest_prob <= 1 and 0 <= sensitivity <= 1 and 0 <= specificity <= 1):
        raise ValueError('Probabilities must be between 0 and 1')
        
    if test_result:
        # Positive test result
        likelihood_ratio = sensitivity / (1 - specificity)
    else:
        # Negative test result
        likelihood_ratio = (1 - sensitivity) / specificity
        
    # Convert probability to odds
    pretest_odds = pretest_prob / (1 - pretest_prob)
    
    # Apply likelihood ratio
    posttest_odds = pretest_odds * likelihood_ratio
    
    # Convert odds back to probability
    posttest_prob = posttest_odds / (1 + posttest_odds)
    
    return posttest_prob