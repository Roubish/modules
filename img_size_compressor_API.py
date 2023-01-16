from fastapi import FastAPI, File, UploadFile,Form
from fastapi.responses import HTMLResponse,StreamingResponse
from typing import List
import os
from PIL import Image
import uvicorn

cwd = os.getcwd()
app = FastAPI()

@app.post('/compress_img/')
async def create_upload_files(files: List[UploadFile] = File(...),ratio : int = Form(...)):
    if ratio is None:
        ratio = 30
    else:
        ratio = 100-ratio
    file_list = [file for file in files]
    for file in file_list:
        image_file = await file.read()
        file_location = f"{cwd}/{file.filename}"

        with open(file_location, "wb+") as file_object:
            file_object.write(image_file)
        
        org_size = os.path.getsize(file_location)/1000
        if org_size<1024:
            org_size = f'{org_size} KB'
        else:
            sz = org_size/1000
            org_size = f'{sz} MB'                               
        img = Image.open(file_location)
        name1 = file.filename
        name = '.'.join(nm for nm in name1.split('.')[:-1])
        filename = f"Compressed_{name}.jpg"
        img.save(filename, 
                     "JPEG", 
                     optimize = True, 
                     quality = 150)
        #os.remove(filename)
        comp_loc = os.path.join(os.getcwd(),filename)
        Compressed_size = os.path.getsize(comp_loc)/1000
        if Compressed_size<1024:
            Compressed_size = f'{Compressed_size} KB'
        else:
            sz = Compressed_size/1000
            Compressed_size = f'{sz} MB'
            
        def iterfile():
          with open(filename, mode="rb") as file_like:  
              yield from file_like  
        return {'Image':comp_loc,'Original Size':org_size,'Compressed Size':Compressed_size,'Ratio':90}
        #return StreamingResponse(iterfile(), media_type=str(file.content_type))

@app.get("/")
async def main():
    content = """
<body>
<form action="/compress_img/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple><br><br>
<label for="fname">Ratio:</label>
<input type="number" id="fname" name="fname"><br><br>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

# =============================================================================
# 
# if __name__ == "__main__":
#     uvicorn.run("main:app", host='127.0.0.1', port=8080,reload=True)
# 
# =============================================================================

