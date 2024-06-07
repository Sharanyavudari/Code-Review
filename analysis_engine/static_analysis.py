# analysis_engine/static_analysis.py

def analyze_static(code):
    # Perform static analysis
    vulnerabilities = []
    quality_issues = []

    # Check for command injection vulnerability
    if "subprocess.check_output(" in code:
        vulnerabilities.append("Command injection vulnerability detected")

    # Check for SQL injection vulnerability
    if "execute_query(" in code:
        vulnerabilities.append("SQL injection vulnerability detected")

    # Check for XSS vulnerability
    if "document.write(" in code:
        vulnerabilities.append("Cross-Site Scripting (XSS) vulnerability detected")

    # Check for quality issues
    if "print(" in code:
        quality_issues.append("Use of print statement (consider using logging module)")

    if "eval(" in code:
        quality_issues.append("Use of eval function (consider safer alternatives)")

    # If no vulnerabilities or quality issues detected, provide appropriate messages
    if not vulnerabilities:
        vulnerabilities.append("No vulnerabilities detected")
    if not quality_issues:
        quality_issues.append("No quality issues detected")

    return {'vulnerabilities': vulnerabilities, 'quality_issues': quality_issues}
