"""
Flora and fauna references compiled from the five uploaded text files.

The lists contain identifiable plant and animal names found in the texts and
are grouped by broad category. Common-name variants are retained where useful.
This is a source-based working inventory, not a taxonomic checklist: generic
terms (for example, "bird" or "fish") are included only where they are useful
as text mentions, and some broad groups may overlap.
"""

SOURCES = ['The Fall of the Sparrow — Nigel Balchin', 'The God of Small Things — Arundhati Roy', 'The Palace of Illusions — Chitra Banerjee Divakaruni', "Nature's Spokesman: M. Krishnan and Indian Wildlife — M. Krishnan / Ramachandra Guha", 'Indica: A Deep Natural History of the Indian Subcontinent — Pranay Lal']

FLORA = ['algae', 'angiosperms', 'Amborella', 'Ceratophyllum', 'cycads', 'Dicroidium', 'ferns', 'tree ferns', 'fungi', 'Prototaxites', 'Aspidella', 'Cooksonia', 'moss', 'Glossopteris', 'Gangamopteris', 'grasses', 'magnolias', 'lotus', 'water lily', 'hyacinth', 'conifers', 'ginkgoes', 'mangroves', 'neem', 'Argemone mexicana', 'tapioca', 'pepper vine', 'mango', 'jackfruit', 'banana', 'red banana', 'tamarind', 'palmyra', 'bamboo', 'sago palm', 'tuber', 'wild creepers', 'laterite vegetation']

FAUNA = ['aardvark', 'white stork', 'stork', 'gecko', 'toad', 'sparrow', 'crow', 'rat snake', 'bullfrog', 'mongoose', 'bat', 'spider', 'bee', 'ant', 'beetle', 'fly', 'moth', 'butterfly', 'wasp', 'scorpion', 'fish', 'ray-finned fish', 'Amblypterus', 'Gardinerichthys', 'Kashmirosaurus', 'Lysipterigium', 'caecilian', 'Thrinaxodon', 'Proterosuchus', 'Parasuchus hislopi', 'Malerisaurus robinsonae', 'Exaeretodon statisticae', 'Endothiodon', 'Rechnisaurus', 'Wadiasaurus', 'Laevisuchus', 'Chasmosaurus', 'Titanis', 'pterosaur', 'Campylognathus', 'Quetzalcoatlus', 'ichthyosaur', 'crocodile', 'gharial', 'turtle', 'lizard', 'snake', 'monitor lizard', 'python', 'cobra', 'tiger', 'lion', 'elephant', 'cheetah', 'sloth bear', 'blackbuck', 'bustard', 'bandicoot', 'desert fox', 'sambar', 'rhinoceros', 'rhino', 'whale', 'dolphin', 'deer', 'mouse', 'shrew', 'marmoset', 'galago', 'jackal', 'horse', 'wolf', 'hyena', 'civet', 'toddy cat', 'panda', 'bear', 'linsang', 'Prionodon pardicolor', 'dire wolf', 'sabre-toothed cat', 'crows', 'bluebottle', 'small fish', 'frog', 'rat', 'housefly', 'mosquito', 'snail', 'crab', 'crustacean', 'bird', 'monkey', 'dog', 'cat', 'pariah dog', 'sloth']

# Optional convenience view
ALL_REFERENCES = {
    "flora": FLORA,
    "fauna": FAUNA,
}

if __name__ == "__main__":
    print("SOURCES")
    for source in SOURCES:
        print(f"- {source}")
    print(f"\\nFLORA ({len(FLORA)} entries)")
    for item in FLORA:
        print(f"- {item}")
    print(f"\\nFAUNA ({len(FAUNA)} entries)")
    for item in FAUNA:
        print(f"- {item}")
