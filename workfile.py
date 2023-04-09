import cohere
import openai
import requests
from cohere.responses.classify import Example

cohereai_api = 'jiVVfDp486Fug9leuHm9yxzmdxwxiaFAc5rS44Mb'
openai_api = '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'

# find hospitals using cohere ai
def func_hospital_find(disease, city, country):
    co = cohere.Client(cohereai_api)  # This is your trial API key
    response = co.generate(
        model='command-medium-nightly',
        prompt=f'suggest me five best {disease} disease hospitals in {city}, {country}.\n',
        max_tokens=500,
        temperature=0.9,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    return '{}'.format(response.generations[0].text)

# finding information using cohere ai
def func_disease_read(disease):
    co = cohere.Client('jiVVfDp486Fug9leuHm9yxzmdxwxiaFAc5rS44Mb')  # This is your trial API key
    response = co.generate(
        model='command-medium-nightly',
        prompt=f'write me an essay about {disease} disease, 100 words.',
        max_tokens=1502,
        temperature=2,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    return '{}'.format(response.generations[0].text)

# summarazing using open ai
def func_essay_summarize(essay):
    openai.api_key = openai_api
    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""summarize this essay: {essay}""",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return response.choices[0].text

def func_classify_disease(essay):
    co = cohere.Client('jiVVfDp486Fug9leuHm9yxzmdxwxiaFAc5rS44Mb')  # This is your trial API key
    response = co.classify(
        model='large',
        inputs=[
            essay],
        examples=[Example(
            "Influenza: caused by the influenza virus, which spreads through respiratory droplets and can cause fever, cough, and body aches.",
            "infectious diseases"), Example(
            "Tuberculosis: caused by the Mycobacterium tuberculosis bacteria, which spreads through airborne droplets and can affect the lungs and other organs.",
            "infectious diseases"), Example(
            "HIV/AIDS: caused by the human immunodeficiency virus (HIV), which attacks the immune system and can lead to acquired immunodeficiency syndrome (AIDS).",
            "infectious diseases"), Example(
            "Malaria: caused by the Plasmodium parasite, which spreads through infected mosquito bites and can cause fever, chills, and other flu-like symptoms.",
            "infectious diseases"), Example(
            "Cholera: caused by the Vibrio cholerae bacteria, which spreads through contaminated water and can cause severe diarrhea and dehydration.",
            "infectious diseases"), Example(
            "Measles: caused by the measles virus, which spreads through respiratory droplets and can cause fever, rash, and other flu-like symptoms.",
            "infectious diseases"), Example(
            "Hepatitis B: caused by the hepatitis B virus, which spreads through bodily fluids and can cause liver inflammation and damage.",
            "infectious diseases"), Example(
            "Zika: caused by the Zika virus, which spreads through mosquito bites and can cause fever, rash, and other flu-like symptoms.",
            "infectious diseases"), Example(
            "Typhoid fever: caused by the Salmonella typhi bacteria, which spreads through contaminated food and water and can cause fever, abdominal pain, and other symptoms.",
            "infectious diseases"), Example(
            "Dengue fever: caused by the dengue virus, which spreads through infected mosquito bites and can cause fever, headache, and severe joint and muscle pain.",
            "infectious diseases"), Example(
            "Beriberi: caused by a deficiency of thiamine (vitamin B1), which is commonly found in whole grains, meat, and legumes.",
            "deficiency diseases"), Example(
            "Scurvy: caused by a deficiency of vitamin C, which is commonly found in citrus fruits, strawberries, and broccoli.",
            "deficiency diseases"), Example(
            "Rickets: caused by a deficiency of vitamin D, which is commonly found in sunlight, fortified dairy products, and fatty fish.",
            "deficiency diseases"), Example(
            "Pellagra: caused by a deficiency of niacin (vitamin B3), which is commonly found in meat, fish, and whole grains.",
            "deficiency diseases"), Example(
            "Night blindness: caused by a deficiency of vitamin A, which is commonly found in liver, sweet potatoes, and carrots.",
            "deficiency diseases"), Example(
            "Goiter: caused by a deficiency of iodine, which is commonly found in seaweed, iodized salt, and seafood.",
            "deficiency diseases"), Example(
            "Anemia: caused by a deficiency of iron, which is commonly found in red meat, beans, and fortified cereals.",
            "deficiency diseases"), Example(
            "Hypocalcemia: caused by a deficiency of calcium, which is commonly found in dairy products, leafy green vegetables, and fortified foods.",
            "deficiency diseases"), Example(
            "Kwashiorkor: caused by a deficiency of protein, which is commonly found in meat, fish, and dairy products.",
            "deficiency diseases"), Example(
            "Hypokalemia: caused by a deficiency of potassium, which is commonly found in bananas, leafy green vegetables, and potatoes.",
            "deficiency diseases"), Example(
            "Cystic Fibrosis: a genetic disorder that affects the lungs, pancreas, and other organs, causing thick mucus buildup that can lead to infections and breathing problems.",
            "hereditary diseases"), Example(
            "Huntington\'s Disease: a neurodegenerative disorder that affects movement, cognition, and behavior, caused by a genetic mutation.",
            "hereditary diseases"),
                  Example("Hemophilia: a bleeding disorder caused by a genetic deficiency in blood clotting factors.",
                          "hereditary diseases"), Example(
                "Sickle Cell Anemia: a blood disorder that causes abnormal red blood cells, which can lead to anemia, pain, and other complications.",
                "hereditary diseases"), Example(
                "Tay-Sachs Disease: a rare, inherited disorder that progressively destroys nerve cells in the brain and spinal cord, leading to developmental delays, blindness, and other symptoms.",
                "hereditary diseases"), Example(
                "Down Syndrome: a genetic disorder caused by an extra copy of chromosome 21, which can lead to developmental delays, intellectual disability, and other health issues.",
                "hereditary diseases"), Example(
                "Muscular Dystrophy: a group of genetic disorders that cause progressive muscle weakness and wasting.",
                "hereditary diseases"), Example(
                "Phenylketonuria (PKU): a genetic disorder that affects the body\'s ability to process the amino acid phenylalanine, which can lead to intellectual disability and other health problems.",
                "hereditary diseases"), Example(
                "Wilson\'s Disease: a genetic disorder that causes the body to retain too much copper, leading to liver and neurological problems.",
                "hereditary diseases"), Example(
                "Celiac Disease: an autoimmune disorder caused by an intolerance to gluten, a protein found in wheat, barley, and rye, which can lead to digestive problems and other health issues.",
                "hereditary diseases"), Example(
                "Diabetes Mellitus: A metabolic disorder characterized by high blood glucose levels due to either insufficient insulin production or insulin resistance.",
                "physiological diseases"), Example(
                "Hypertension: High blood pressure, which can cause damage to blood vessels and increase the risk of heart disease and stroke.",
                "physiological diseases"), Example(
                "Asthma: A chronic respiratory disease characterized by inflammation and narrowing of the airways, leading to wheezing, coughing, and difficulty breathing.",
                "physiological diseases"), Example(
                "Arthritis: A group of diseases that cause inflammation and pain in the joints, leading to stiffness and limited mobility.",
                "physiological diseases"), Example(
                "Chronic Obstructive Pulmonary Disease (COPD): A chronic lung disease that includes chronic bronchitis and emphysema, leading to difficulty breathing and a reduced ability to perform physical activities.",
                "physiological diseases"), Example(
                "Cardiovascular Disease: A group of diseases that affect the heart and blood vessels, including coronary artery disease, heart failure, and stroke.",
                "physiological diseases"), Example(
                "Osteoporosis: A disease that weakens bones and increases the risk of fractures, often associated with aging and hormonal changes.",
                "physiological diseases"), Example(
                "Alzheimer\'s Disease: A progressive neurological disorder that affects memory, thinking, and behavior, and can ultimately lead to severe cognitive impairment.",
                "physiological diseases"), Example(
                "Parkinson\'s Disease: A degenerative disorder of the nervous system that affects movement, balance, and coordination.",
                "physiological diseases"), Example(
                "Multiple Sclerosis: A chronic autoimmune disease that affects the central nervous system, leading to a wide range of symptoms including fatigue, muscle weakness, and difficulty with coordination and balance.",
                "physiological diseases")])
    return response.classifications[0].prediction

def image_generator(topic):
    try:
        openai.api_key = openai_api
        response = openai.Image.create(
            prompt=topic,
            n=1,
            size="256x256"
            )
        image_url = response['data'][0]['url']
    except Exception as ex:
        image_url = str(ex)
    return image_url
