from grobid_client.grobid_client import GrobidClient

client = GrobidClient(config_path="./config.json")
client.process("processFulltextDocument", "./Files/*",  output="./Files/test_out/" , n=20)
