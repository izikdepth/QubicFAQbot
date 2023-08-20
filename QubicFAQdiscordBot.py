import os
import discord
import discord.ext
from dotenv import load_dotenv
import json
import requests
import logging




load_dotenv()

#intents
intents = discord.Intents.all() 

#set prefix
# bot = commands.Bot(command_prefix='/', intents=intents,  help_command=None) #command prefix

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

#logging
logging.basicConfig(level=logging.INFO, filename="qubicfaqbot_log.log", format="%(asctime)s %(levelname)s: %(message)s")

#to track users who have interacted with the bot
user_interactions = {}





# @bot.event
# async def on_ready():
#     logging.info(f"Logged in as {bot.user.name} - {bot.user.id}")
#     logging.info(f"Total user interactions: {sum(user_interactions.values())}")
#     logging.info(f"Unique users: {len(user_interactions)}")
@client.event
async def on_ready():
    await tree.sync()
    print("ready")
    logging.info(f"Logged in as {client.user.name} - {client.user.id}")
    logging.info(f"Total user interactions: {sum(user_interactions.values())}")
    logging.info(f"Unique users: {len(user_interactions)}")
    



@tree.command(name="start", description="description")
async def slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    await interaction.response.send_message("You've now activated Qubic's FAQ bot. use command /help to view available commands")

@tree.command(name="otc", description="description")
async def slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "*Seller and Buyer agree to a Deal*\n\n"
        "1. *Seller* transfers qus to escrow account of *Escrowee*\n"
        "2. *Escrowee* will inform *Buyer* as soon as tx has been confirmed (qus deposited on account)\n"
        "3. *Buyer* transfers bitcoin or any other currency to *Sellers* account\n"
        "4. *Escrowee* checks if the transaction has been confirmed. *Seller* confirms receipt to *Escrowee*\n"
        "5. *Escrowee* releases qus from escrow account to *Buyers* account\n\n"
        "what we ensure:\n"
        "- the amount of qus are real and written to ledger during escrow service\n"
        "- if the seller does not confirm the payment but we have enough confirmations (e.g. btc 3-4) the qus will be released\n"
        "- if the buyer doesn't pay, the seller will get its qus back\n\n"
        "what we offer:\n"
        "- protection of seller and buyer\n"
        "- if wished anonymity for both sides\n"
        "- help to understand how qubic work\n"
        "- help to set up and secure a qubic address\n\n"
        "and all of that we do with a smile for you. *ask us to mark one of your posts in the qubic channel with a reaction to be sure that you are speaking with the right person.*"
    )
    await interaction.response.send_message(message) 
    

@tree.command(name="ai", description="description")
async def slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
    "Real AI, also known as Artificial General Intelligence (AGI),\n"
    "refers to a type of artificial intelligence that has the ability to understand, learn,\n"
    "adapt, and implement knowledge across a broad range of tasks at a level equal to or beyond human capabilities.\n"
    "Qubic's design allows for the development and deployment of scalable AGI solutions,\n"
    "powered by its unique computational and economic model.\n"
    "Learn more about AGI with this [Medium article](https://medium.com/@comefrombeyond/introduction-of-aigarth-f40e741e256c)."
    )
    await interaction.response.send_message(message) 
    
@tree.command(name="founder", description="description")
async def slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "The main developer behind Qubic is Sergey Ivancheglo (also known as Come-From-Beyond or CFB), "
        "a co-founder of NXT, IOTA, and a prominent figure in the crypto community. "
        "The exact composition of the entire development team might vary over time.\n\n"
        "Learn more about Sergey Ivancheglo (CFB) at: [CFB's Website](https://come-from-beyond.okis.ru/)"
    )
    await interaction.response.send_message(message)
    
@tree.command(name="history", description="description")
async def slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "Qubic history:\n"
        "- Qubic dates back to 2012. Check out the discussion on [bitcointalk.org](https://bitcointalk.org/index.php?topic=112676.0)\n"
        "- Series of Medium articles 'Qubic: Quorum-based Computations — Powered by IOTA' from 2018 - some parts may have changed but some remain true:\n"
        "  1. [INTRODUCTION](https://medium.com/coinmonks/qubic-quorum-based-computations-powered-by-iota-3770fbd62341)\n"
        "  2. [Oracles & quorums](https://medium.com/coinmonks/qubic-quorum-based-computations-powered-by-iota-52e13c46bdde)\n"
        "  3. [Deep dive into qubics](https://medium.com/coinmonks/qubic-quorum-based-computations-powered-by-iota-66aa61ca4916)\n"
        "  4. [The Qubic Protocol](https://medium.com/coinmonks/qubic-quorum-based-computations-powered-by-iota-bb58432baea)\n"
        "  5. [Roadmap](https://medium.com/coinmonks/qubic-quorum-based-computations-powered-by-iota-51c8517d0c57)"
    )
    await interaction.response.send_message(message)

@tree.command(name="whitepaper", description="description")
async def slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "[WHITEPAPER](https://docs.qubic.world/overview/whitepaper/)"
    )
    await interaction.response.send_message(message)
    
@tree.command(name="docs", description="description")
async def slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = "1. [OFFICIAL DOCS](https://docs.qubic.world/)\n2. [COMMUNITY DOCS - still valid](https://qubic-world-2.gitbook.io/welcome-to-gitbook/)"
    await interaction.response.send_message(message)
    
@tree.command(name="wallet", description="description")
async def slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    instructions = (
        "To create a Qubic wallet, follow these steps:\n\n"
        "1. Click the website [Qubic Wallet](https://wallet.qubic.li/)\n"
        "2. You'll be directed to the Qubic wallet page. Select your preferred language.\n"
        "3. Click on 'Create new wallet'.\n"
        "4. Enter a strong password for your wallet and click 'Safe Wallet File'.\n"
        "5. On the dashboard, click 'Add Address'.\n"
        "6. Enter a name for your wallet and click the 'X' icon to reveal your private key.\n"
        "   Make sure to copy your private key in a safe and secure place.\n"
        "7. Click 'Create Address'.\n\n"
        "For more detailed information, check out the [Qubic Wallet Documentation](https://discord.com/channels/768887649540243497/1074609434015322132/1128710949436661932)."
    )
    await interaction.response.send_message(instructions)
    


def get_price(request):
    url = "https://api.livecoinwatch.com/coins/single"
    payload = json.dumps({
      "currency": "USD",
      "code": "QUBIC",
      "meta": True
    })
    
    headers = {
      'content-type': 'application/json',
      'x-api-key': '0d010030-4ec2-4f04-a971-99667a3422b7'
    }
    
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
        price = data['rate']
        return price
    except KeyError:
        return None
    
@tree.command(name="price", description="description")
async def slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    qubic_price = get_price(requests)
    formatted_price = "{:.8f}".format(qubic_price)
    await interaction.response.send_message(f"The current price of QUBIC is: {formatted_price} $")

    
@tree.command(name="node", description="description")
async def slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = ("[GUIDE TO RUN A QUBIC NODE](https://github.com/J0ET0M/qubic-howto)")
    await interaction.response.send_message(message)
    
@tree.command(name="arbitor", description="description")
async def slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "An entity within the Qubic ecosystem responsible for resolving disputes and protecting user interests. "
        "The arbitrator sets parameters of the mining algorithm, publishes lists of computors every epoch, is developing "
        "the capacity to replace faulty computors, and accumulates QUBIC not received by underperforming computors. "
        "Each node operator individually selects their arbitrator by setting the corresponding ID in Qubic.cpp. "
        "The entity controlling the current arbitrator remains unknown, though rumors suggest it's operated by the development team."
    )
    await interaction.response.send_message(message)
    
@tree.command(name="aigarth", description="description")
async def slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "Aigarth is a pioneering project that will be developed on top of the Qubic network. "
        "It combines the fields of artificial intelligence and distributed computing to create a collective system "
        "for solving complex AI tasks. The name \"Aigarth\" is a fusion of \"AI\" for artificial intelligence, "
        "and \"garth,\" an old term for garden or yard.\n\n"
        "**/NOTE/**\n"
        "Aigarth is currently in development and more information will be provided once it's ready to be launched. "
        "Stay tuned to our updates for more information.\n\n"
        "More at https://docs.qubic.world/learn/aigarth\n\n"
        "Since the beginning of artificial neural networks usage researchers were trying to mimic natural brain as "
        "much as possible. Some of them followed the path of mimicking neuron activation function which is very "
        "sophisticated, there are several qualitatively different models, they are impractical to use (because of "
        "integral-differential math of the most complex ones). If you remembered very first years of your life you "
        "would notice that you learned a lot of things and got a lot of mental skills while keeping the same functionality "
        "of neurons. What really changed is the number of connections between them. There are whitepapers researching "
        "properties of \"blank\" ANNs. Their general result: If you initialize an ANN with random parameters you'll "
        "get some primitive cognitive function. An ANN where all neurons are connected to all other neurons already "
        "has memory and some intellect. By destroying connections between neurons you are improving the ANN. After "
        "some point the destruction process starts leading to degradation, so there must be at least one sweet spot "
        "where ANN of certain size has the best IQ. Instead of following the destruction routine we, miners, generate "
        "ANNs with random structure of connections. We change parameters of this generation and Aigarth analyzes "
        "properties of the ANNs. At the current stage, we are collecting samples trying to get patterns which may "
        "give us insight about further steps to do."
    )
    await interaction.response.send_message(message)
    

    
@tree.command(name="algorithm", description="description")
async def slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "Qubic uses the KangarooTwelve cryptographic hashing algorithm for mining, "
        "with a slight modification which makes it specific to the Qubic network."
    )
    await interaction.response.send_message(message)
    
@tree.command(name="qubicblockchain", description="description")
async def  slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "Qubic is an independent technology that operates on its own blockchain solution. "
        "Through this independent blockchain, Qubic enables an innovative approach, incorporating Quorum "
        "and true finality. This combination ensures high scalability, feeless transactions, and fast operations, "
        "making Qubic a powerful and efficient platform."
    )
    await interaction.response.send_message(message)
    
@tree.command(name="team", description="description")
async def  slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "As of the last update in September 2021, individual team members other than CFB were not explicitly mentioned. "
        "Current information can be found in the official Qubic resources or in the community channels."
    )
    await interaction.response.send_message(message)
    
@tree.command(name="whyupow", description="description")
async def  slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "The concept of Useful Proof of Work (UPoW) represents an evolution in the conventional Proof of Work (PoW) approach. "
        "While traditional PoW algorithms demand computational resources to solve arbitrary mathematical problems as a means to "
        "validate transactions and secure the network, UPoW redirects these resources towards solving meaningful and valuable "
        "problems. In Qubic, UPoW is used to contribute to artificial intelligence (AI) training tasks. This means that the "
        "computational power of the network isn't just used for maintaining the network's integrity, but also for advancing AI "
        "capabilities. It represents a more efficient use of resources and adds value to the network beyond just transaction "
        "processing. Furthermore, by integrating UPoW within its ecosystem, Qubic fosters a more productive and beneficial "
        "network that directly contributes to technological advancement. This model can attract more participants to the network, "
        "strengthening the network's security, and generating practical, real-world value."
    )
    await interaction.response.send_message(message)
    
@tree.command(name="upow", description="description")
async def  slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "Proof of Work (PoW) is a fundamental concept employed across various computer sciences and particularly in the realm "
        "of cryptocurrencies, where it ensures the security and reliability of decentralized networks like Bitcoin. It accomplishes "
        "this by making the process of altering or creating fraudulent transactions computationally expensive and time-consuming. "
        "However, in the innovative Qubic ecosystem, we've introduced an exciting twist on the traditional PoW by integrating AI "
        "training as a means of achieving the same consensus, giving rise to a novel consensus mechanism: Useful Proof of Work (UPoW)."
    )
    await interaction.response.send_message(message)
    
@tree.command(name="oracles", description="description")
async def  slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "Oracles in Qubic serve as a bridge between the digital blockchain environment and the outside world. "
        "They provide real-world data to smart contracts and the Qubic protocol. These could be anything from "
        "stock market prices, weather data, or IoT sensor readings. The ability to securely integrate external "
        "data significantly broadens the use-cases for Qubic smart contracts."
    )
    await interaction.response.send_message(message)
    
@tree.command(name="whyqubic", description="description")
async def  slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "Smart Contracts (SC) on Qubic are truly remarkable as they harness the power of Qubic Units (QUBIC) "
        "as 'energy' to facilitate contract execution. Unlike traditional Smart Contracts, Qubic SCs are "
        "frictionless and highly scalable, effectively reducing inflation by 'burning' the QUBIC used in their execution. "
        "Additionally, Qubic SCs have the extraordinary ability to incorporate real-world data through Qubic's oracles, "
        "significantly enhancing their utility and applicability.\n\n"
        "A fascinating aspect is that the execution of SCs consumes QUBIC, yet remains free for users as the SC self-finances "
        "through funds collected during its Initial Coin Offering. However, SCs also have the option to request QUBIC from users "
        "for their services, offering a dynamic and flexible approach to their functionality.\n\n"
        "In summary, Qubic revolutionizes the concept of Smart Contracts with these innovative features, making them more efficient "
        "and adaptable to real-world needs. By allowing integration of external data sources, Qubic SCs open up new possibilities "
        "for decentralized applications, bringing us closer to a future with improved efficiency and seamless interactions on the blockchain."
    )
    await interaction.response.send_message(message)
    
@tree.command(name="gpumining", description="description")
async def  slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "Yes, it is possible, but it is not particularly effective compared to using a CPU. "
        "For this reason, it is more advisable to use a CPU to achieve the desired mining performance."
    )
    await interaction.response.send_message(message)
    
    
@tree.command(name="cpumining", description="description")
async def slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "In this case, it has been found that mining on the CPU is more effective. "
        "This is because the mining algorithm used benefits from the parallel processing of multiple CPU cores, resulting in higher efficiency."
    )
    await interaction.response.send_message(message)
 
@tree.command(name="transactiontimeout", description="description")
async def  slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
        "Every transaction includes the number of the tick in which it can be processed. "
        "If that tick has passed and the transaction hasn't been processed, it will need to be repeated. "
        "Unlike in other blockchain solutions, this feature prevents transactions from being pending indefinitely "
        "and ensures more predictability in the transaction process."
    )
    await interaction.response.send_message(message)
    
@tree.command(name="manageseed", description="description")
async def  slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    instructions = (
        "Your seed acts as your password, similar to a private key in Bitcoin.\n"
        "It's confidential and should be securely stored at all times.\n\n"
        "🛑  **/CAUTION/** 🛑\n"
        "Never share your seed with anyone. If you lose it, you'll lose access to your Qubic Units (QUs).\n"
        "The seed must consist of 55 lowercase letters. Simply generate it randomly.\n\n"
        "Here's an example of a seed:\n"
        "abchvbvddggkjfnokduyjuiyvkklrvrmsaozwbvjlzvgvfipqpnkkuf\n\n"
        "For more detailed information, check out the [Investment Guide](https://docs.qubic.world/learn/invest)."
    )
    await interaction.response.send_message(instructions)
    
    
@tree.command(name="maxsupply", description="description")
async def  slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
    "The maximum supply of Qubic coin $Qu is 100 Trillion.\n"
    "Confirmation from [founder](https://twitter.com/c___f___b/status/1690411278387363840?s=20)."
)
    await interaction.response.send_message(message)
    
 
@tree.command(name="help", description="description")
async def  slash_command(interaction:discord.Interaction):
    logging.info(f"{interaction.user} used the {interaction.command} command")  # Log command usage
    message = (
    "Here are the available commands:\n\n"
    "1. /help - Check available commands\n"
    "2. /ai - Learn more about AI and its relation to QUBIC\n"
    "3. /otc - Learn how to buy $qu via OTC\n"
    "4. /founder - Learn more about the Founder (come_from_beyond)\n"
    "5. /history - Learn the history of Qubic\n"
    "6. /whitepaper - View the whitepaper\n"
    "7. /docs - View documentation and learn more about the project\n"
    "8. /node - guide on how to run a node\n"
    "9. /arbitor - what is an arbitor\n"
    "10. /aigarth - learn about Aigarth\n"
    "11. /algorithm - what algorithm does Qubic use?\n"
    "12. /qubicblockchain - what blockchains use qubic?\n"
    "13. /team - who are the team members of Qubic blockchain?\n"
    "14. /whyupow- why UPow?\n"
    "15. /upow - what is Useful Proof of Work?\n"
    "16. /oracles - oracles\n"
    "17. /whyqubic - what's new about Qubic blockchain?\n"
    "18. /gpumining - can I use GPU to mine?\n"
    "19. /cpumining - mining Qubic coins with CPU\n"
    "20. /transactiontimeout - what happens when my transaction fails?\n"
    "21. /wallet - how to create a wallet\n"
    "22. /manageseed - how to manage your seed\n"
    "23. /price - to check the price of Qubic\n"
    "24. /maxsupply - to check the maximum supply\n")
    
    await interaction.response.send_message(message)


     
# run the bot
client.run(os.getenv("DISCORD_TOKEN"))     
