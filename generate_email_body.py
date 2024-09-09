import random

def generate_body(all_dfs, sender_name):
    with open('email.html', 'r') as file:
        # Read the entire content of the file
        html_content = file.read()

    # Now 'all_dfs' is a dictionary where keys are sheet names and values are DataFrames
    # Access each DataFrame using the corresponding sheet name

    subjects_df = all_dfs['subjects']
    introductions_df = all_dfs['introductions']
    p2_heading_df = all_dfs['p2_heading']
    p2_para_df = all_dfs['p2_para']
    p3_heading_df = all_dfs['p3_heading']
    p3_para_df = all_dfs['p3_para']
    p4_heading_df = all_dfs['p4_heading']
    p4_para_df = all_dfs['p4_para']
    p5_para_heading_df = all_dfs['5th_para_heading']
    p5_para_df = all_dfs['5th_para']
    reply_to_this_mail_heading_df = all_dfs['reply_to_this_mail_heading']
    reply_to_this_email_df = all_dfs['reply_to_this_email']
    thanks_last_df = all_dfs['thanks_last']

    # Randomly select a single value from each specified column
    selected_subject = subjects_df['subjects'].sample().iloc[0]
    selected_introduction = introductions_df['introductions'].sample().iloc[0]
    selected_p2_heading = p2_heading_df['p2_heading'].sample().iloc[0]
    selected_p2_para = p2_para_df['p2_para'].sample().iloc[0]
    selected_p3_heading = p3_heading_df['p3_heading'].sample().iloc[0]
    selected_p3_para = p3_para_df['p3_para'].sample().iloc[0]
    selected_p4_heading = p4_heading_df['p4_heading'].sample().iloc[0]
    selected_p4_para = p4_para_df['p4_para'].sample().iloc[0]
    selected_p5_para_heading = p5_para_heading_df['5th_para_heading'].sample().iloc[0]
    selected_p5_para = p5_para_df['5th_para'].sample().iloc[0]
    selected_reply_to_this_mail_heading = reply_to_this_mail_heading_df['reply_to_this_mail_heading'].sample().iloc[0]
    selected_reply_to_this_email = reply_to_this_email_df['reply_to_this_email'].sample().iloc[0]
    selected_thanks_last = thanks_last_df['thanks_last'].sample().iloc[0]

    mail_subject = selected_subject
    mail_subject = selected_subject.replace('Raju Ahammod', sender_name)
    html_content = html_content.replace("#selected_subject#", selected_subject)
    html_content = html_content.replace("#selected_introduction#", selected_introduction)
    html_content = html_content.replace("#selected_p2_heading#", selected_p2_heading.upper())
    html_content = html_content.replace("#selected_p2_para#", selected_p2_para)
    html_content = html_content.replace("#selected_p3_para#", selected_p3_para)
    html_content = html_content.replace("#selected_p3_heading#", selected_p3_heading.upper())
    html_content = html_content.replace("#selected_p4_heading#", selected_p4_heading.upper())
    html_content = html_content.replace("#selected_p4_para#", selected_p4_para)
    html_content = html_content.replace("#selected_p5_para_heading#", selected_p5_para_heading.upper())
    html_content = html_content.replace("#selected_p5_para#", selected_p5_para)
    html_content = html_content.replace("#selected_reply_to_this_mail_heading#", selected_reply_to_this_mail_heading.upper())
    html_content = html_content.replace("#selected_reply_to_this_email#", selected_reply_to_this_email)
    html_content = html_content.replace("#selected_thanks_last#", selected_thanks_last)
    html_content = html_content.replace("#new_line#", '\n')
    html_content = html_content.replace("#added_tab#", '\t')
    html_content = html_content.replace('RAJU AHAMMOD', sender_name)

    return html_content, mail_subject


