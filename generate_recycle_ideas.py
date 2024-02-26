import google.generativeai as genai
import PIL.Image

GOOGLE_API_KEY='AIzaSyDWlRdJLFr7v9nUWmADlypMM3CkPhc1_5U'

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro-vision')



images = []


nsamples = 10

for i in range(nsamples):
    filename = f"images_and_examples/image{i+1}.JPG"
    img = PIL.Image.open(filename)
    images.append(img)

with open('images_and_examples/example1.txt', 'r') as file:
    example1 = file.read()
with open('images_and_examples/example2.txt', 'r') as file:
    example2 = file.read()

for j in range(3):
  example = ""
  run = "zero shot"
  if j == 1:
    run = "one shot"
    example ="Here is an example:"+ example1
  if j == 2:
    run = "few shot"
    example ="Here are multiple examples:"+example2
  for i in range(nsamples):
    response = model.generate_content(["Based on the image of an item provided by the user, which represents a product they wish to recycle, repurpose, or upcycle, please analyze the item and generate one innovative and practical idea for extending its lifecycle. Your suggestions should focus on creative uses that go beyond traditional recycling methods, especially for items not typically considered recyclable. After identifying a potential new use, provide a detailed step-by-step guide on how the user can transform the item from its current state into the new, repurposed form. Your recommendations should be feasible for the average person to accomplish with common tools and materials. Please draw from your extensive database of knowledge to ensure the ideas are both unique and practical, highlighting any specific techniques or materials needed for the transformation."+example, images[i]], stream=True)
    response.resolve()
    with open(run+"_"+str(i)+'.txt', 'w') as file:
      file.write(response.text)
