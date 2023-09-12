from transformers import pipeline

translator = pipeline(model= "saikiranmaddukuri/chat_to_sql0.17")
text='question:Find the name of services that have been used for more than 2 times in first notification of loss. table:CREATE TABLE services (service_name VARCHAR, service_id VARCHAR); CREATE TABLE first_notification_of_loss (service_id VARCHAR)'
print(translator([text]))