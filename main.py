import my_vector_search as my_vector_search
import my_chatgpt as my_chatgpt
import textwrap
import my_speech_recognizer

def main():
 
    print ("Hello. Can i help you with book recommendations based on your areas of interest?")
    summary = my_chatgpt.chat()
    
    #user_input = "I am looking for book recommendations for 12 year old girl who is interested in fiction. She loves wings of fire book series. But i would like her to try something new now. Can you please recommend a suitable book for her."
    #prompt = "Summarize the following text in instruction format. Provide summary in one sentence" 
    #summary = my_chatgpt_old.summarize_text(user_input,prompt)
    print("Search String : ",summary)

    books_list, books = my_vector_search.search_data_in_csv("books_cleaned.csv","tagged_description",summary)
    print (books[books["isbn13"].isin(books_list)]) 

''''voice = my_speech_recognizer.speech_to_text()
print (voice)'''

if __name__ == "__main__":
  main()