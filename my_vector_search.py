from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
import logging
import os
import pandas as pd

def convert_csv_col_to_docs(csv_file,col_name):
        print ("inside csv to docs function")

        # Disable the warning messages
        logging.getLogger("langchain_text_splitters.base").setLevel(logging.ERROR)

        txt_file = col_name + ".txt"
        dframe = pd.read_csv(csv_file)
        dframe[col_name].to_csv(txt_file,lineterminator= '\n',index = False,header = False)
        raw_documents = TextLoader(txt_file).load()
        text_splitter = CharacterTextSplitter(chunk_size=0, chunk_overlap=0, separator="\n")
        docs = text_splitter.split_documents(raw_documents)
        return docs , dframe

def retrieve_semantic_recommendations(
        documents,
        query: str,
        top_k: int = 10,
) -> pd.DataFrame:
        print ("inside semantic search function")
        search_db = Chroma.from_documents(
        documents,
        embedding=OpenAIEmbeddings())

        recs = search_db.similarity_search(query, k = 50)
        result_list = []
        for i in range(0, len(recs)):
            result_list += [int(recs[i].page_content.strip('"').split()[0])]
        return result_list

def search_data_in_csv(csv_file_name,search_column,search_query):
        print ("inside search_data_in_csv")
        search_documents , csv_dframe = convert_csv_col_to_docs(csv_file_name,search_column)
        load_dotenv()
        print("API key - ",os.environ.get("OPENAI_API_KEY"))
        search_results_list = retrieve_semantic_recommendations(search_documents,search_query)
        return search_results_list, csv_dframe