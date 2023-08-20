from telegram.ext import Application, CommandHandler, MessageHandler, filters, Updater
from dotenv import load_dotenv
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
import json
import requests
import decimal
import locale


load_dotenv()

async def start(update, context):
    await update.message.reply_text("You've now activated Qubic's FAQ Bot. Use /help to view commands.")
    

async def otc(update, context):
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
    await update.message.reply_text(message, parse_mode="Markdown")


    
async def AI(update, context):
    message = (
        "Real AI, also known as Artificial General Intelligence (AGI),\n"
        "refers to a type of artificial intelligence that has the ability to understand, learn,\n"
        "adapt, and implement knowledge across a broad range of tasks at a level equal to or beyond human capabilities.\n"
        "Qubic's design allows for the development and deployment of scalable AGI solutions,\n"
        "powered by its unique computational and economic model.\n"
        "Learn more about AGI with this [Medium article](https://medium.com/@comefrombeyond/introduction-of-aigarth-f40e741e256c)."
    )
    await update.message.reply_text(message)


    
async def founder(update, context):
    message = (
        "The main developer behind Qubic is Sergey Ivancheglo (also known as Come-From-Beyond or CFB), "
        "a co-founder of NXT, IOTA, and a prominent figure in the crypto community. "
        "The exact composition of the entire development team might vary over time.\n\n"
        "Learn more about Sergey Ivancheglo (CFB) at: [CFB's Website](https://come-from-beyond.okis.ru/)"
    )
    await update.message.reply_text(message)

async def history(update, context):
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
    await update.message.reply_text(message)

    
async def whitepaper(update, context):
    text = "Check out the Qubic Whitepaper"
    url = "https://docs.qubic.world/overview/whitepaper/"
    
    button = InlineKeyboardButton(text, url=url)
    
    keyboard = [[button]]  # List of lists containing the button
    
    markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("Here's the link to the whitepaper:", reply_markup=markup)

    
async def docs(update, context):
    text = "Check out the Qubic Docs"
    url = "https://docs.qubic.world/"
    url2 = "https://qubic-world-2.gitbook.io/welcome-to-gitbook/"
    
    button = InlineKeyboardButton(text, url=url)
    keyboard = [[button]]  # List of lists containing the button
    markup = InlineKeyboardMarkup(keyboard)
    
    message = (
        f"Here's the link to the official docs: [Qubic Docs]({url})\n"
        f"Community made docs: [GitBook]({url2})"
    )
    
    await update.message.reply_text(message, reply_markup=markup, parse_mode="MarkdownV2")


    
async def node(update, context):
    text =  "Guide to run a node with requirements"
    url = "https://github.com/J0ET0M/qubic-howto"
    
    button = InlineKeyboardButton(text, url=url)
    keyboard = [[button]]
    markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("Guide to run a node with requirements:", reply_markup=markup)
    
async def arbitor(update, context):
    message = (
        "An entity within the Qubic ecosystem responsible for resolving disputes and protecting user interests. "
        "The arbitrator sets parameters of the mining algorithm, publishes lists of computors every epoch, is developing "
        "the capacity to replace faulty computors, and accumulates QUBIC not received by underperforming computors. "
        "Each node operator individually selects their arbitrator by setting the corresponding ID in Qubic.cpp. "
        "The entity controlling the current arbitrator remains unknown, though rumors suggest it's operated by the development team."
    )
    await update.message.reply_text(message)

async def aigarth(update, context):
    message = (
        "Aigarth is a pioneering project that will be developed on top of the Qubic network. "
        "It combines the fields of artificial intelligence and distributed computing to create a collective system "
        "for solving complex AI tasks. The name \"Aigarth\" is a fusion of \"AI\" for artificial intelligence, "
        "and \"garth,\" an old term for garden or yard.\n\n"
        "**!NOTE!**\n"
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
    await update.message.reply_text(message)

async def algorithm(update, context):
    message = (
        "Qubic uses the KangarooTwelve cryptographic hashing algorithm for mining, "
        "with a slight modification which makes it specific to the Qubic network."
    )
    await update.message.reply_text(message)

    
async def qubicBlockchain(update, context):
    message = (
        "Qubic is an independent technology that operates on its own blockchain solution. "
        "Through this independent blockchain, Qubic enables an innovative approach, incorporating Quorum "
        "and true finality. This combination ensures high scalability, feeless transactions, and fast operations, "
        "making Qubic a powerful and efficient platform."
    )
    await update.message.reply_text(message)

async def team(update, context):
    message = (
        "As of the last update in September 2021, individual team members other than CFB were not explicitly mentioned. "
        "Current information can be found in the official Qubic resources or in the community channels."
    )
    await update.message.text_reply(message)

async def whyUPoW(update, context):
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
    await update.message.reply_text(message)
    
async def UPoW(update, context):
    message = (
        "Proof of Work (PoW) is a fundamental concept employed across various computer sciences and particularly in the realm "
        "of cryptocurrencies, where it ensures the security and reliability of decentralized networks like Bitcoin. It accomplishes "
        "this by making the process of altering or creating fraudulent transactions computationally expensive and time-consuming. "
        "However, in the innovative Qubic ecosystem, we've introduced an exciting twist on the traditional PoW by integrating AI "
        "training as a means of achieving the same consensus, giving rise to a novel consensus mechanism: Useful Proof of Work (UPoW)."
    )
    await update.message.reply_text(message)
    
async def oracles(update, context):
    message = (
        "Oracles in Qubic serve as a bridge between the digital blockchain environment and the outside world. "
        "They provide real-world data to smart contracts and the Qubic protocol. These could be anything from "
        "stock market prices, weather data, or IoT sensor readings. The ability to securely integrate external "
        "data significantly broadens the use-cases for Qubic smart contracts."
    )
    await update.message.reply_text(message)

async def whyQubic(update, context):
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
    await update.message.reply_text(message)
    
async def gpuMining(update, context):
    message = (
        "Yes, it is possible, but it is not particularly effective compared to using a CPU. "
        "For this reason, it is more advisable to use a CPU to achieve the desired mining performance."
    )
    await update.message.reply_text(message)
    
async def cpuMining(update, context):
    message = (
        "In this case, it has been found that mining on the CPU is more effective. "
        "This is because the mining algorithm used benefits from the parallel processing of multiple CPU cores, resulting in higher efficiency."
    )
    await update.message.reply_text(message)
    
async def transactionTimeout(update, context):
    message = (
        "Every transaction includes the number of the tick in which it can be processed. "
        "If that tick has passed and the transaction hasn't been processed, it will need to be repeated. "
        "Unlike in other blockchain solutions, this feature prevents transactions from being pending indefinitely "
        "and ensures more predictability in the transaction process."
    )
    await update.message.reply_text(message)
    
async def createQubicWallet(update, context):
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
        "For more detailed information, check out the [Qubic Wallet Documentation](https://docs.qubic.world/learn/wallets)."
    )

    button_text = "Visit Qubic Docs"
    docs_url = "https://docs.qubic.world/"
    
    button = InlineKeyboardButton(button_text, url=docs_url)
    keyboard = [[button]]
    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        instructions,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=markup
    )
    
async def manageSeed(update, context):
    instructions = (
        "Your seed acts as your password, similar to a private key in Bitcoin.\n"
        "It's confidential and should be securely stored at all times.\n\n"
        "🛑  **!CAUTION!** 🛑\n"
        "Never share your seed with anyone. If you lose it, you'll lose access to your Qubic Units (QUs).\n"
        "The seed must consist of 55 lowercase letters. Simply generate it randomly.\n\n"
        "Here's an example of a seed:\n"
        "abchvbvddggkjfnokduyjuiyvkklrvrmsaozwbvjlzvgvfipqpnkkuf\n\n"
        "For more detailed information, check out the [Investment Guide](https://docs.qubic.world/learn/invest)."
    )

    button_text = "Visit Qubic Docs"
    docs_url = "https://docs.qubic.world/learn/invest"
    
    button = InlineKeyboardButton(button_text, url=docs_url)
    keyboard = [[button]]
    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        instructions,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=markup
    )
    


async def maxSupply(update, context):
    message = (
        "The maximum supply of Qubic coin $Qu is 100 Trillion.\n"
        "Confirmation from [founder](https://twitter.com/c___f___b/status/1690411278387363840?s=20)."
    )
    
    button_text = "More Info"
    twitter_link = "https://twitter.com/c___f___b/status/1690411278387363840?s=20"
    
    button = InlineKeyboardButton(button_text, url=twitter_link)
    keyboard = [[button]]
    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        message,
        parse_mode="Markdown",
        disable_web_page_preview=False,  # Allow the preview for the button link
        reply_markup=markup
    )
    
# async def CSupply():
    
# async def Mcap():



async def get_price(request):
    url = "https://api.livecoinwatch.com/coins/single"
    payload = json.dumps({
      "currency": "USD",
      "code": "QUBIC",
      "meta": True
    })
    
    headers = {
      'content-type': 'application/json',
      'x-api-key': 'be386cce-0339-4dd0-a510-193c50c03893'
    }
    """
#     get a free API key on https://www.livecoinwatch.com/tools/api
#     """
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
        price = data['rate']
        return price
    except KeyError:
        return None


async def price(update, context):
    qubic_price = await get_price(requests)
    formatted_price = "{:.8f}".format(qubic_price)
    # return formatted_price
    await update.message.reply_text(f"The current price of QUBIC is: {formatted_price} $")
    

async def fdv(update, context):
    total_supply = decimal.Decimal("1000000000000000")
    qubic_price = await get_price(requests)
    
    if qubic_price is not None and isinstance(qubic_price, (int, float, decimal.Decimal)):
        fdv = decimal.Decimal(str(total_supply)) * decimal.Decimal(str(qubic_price))
        
        # Set the locale for formatting
        locale.setlocale(locale.LC_ALL, '')
        
        # Format the fdv variable with commas
        formatted_fdv = "{:,.2f}".format(fdv)
        
        await update.message.reply_text(f"FDV is: {formatted_fdv} $")
    else:
        await update.message.reply_text("Failed to get the QUBIC price.")

 

async def help(update, context):
    message = """
    Here are the available commands:

    1. /help - Check available commands
    2. /AI - Learn more about AI and its relation to QUBIC
    3. /otc - Learn how to buy $qu via OTC
    4. /founder - Learn more about the Founder (come_from_beyond)
    5. /history - Learn the history of Qubic
    6. /whitepaper - View the whitepaper
    7. /docs - View documentation and learn more about the project
    8. /node - guide on how to run a node
    9. /arbitor - what is an arbitor
    10. /aigarth - learn about Aigarth
    11. /algorithm - what algorithm does Qubic use?
    12. /qubicBlockchain - what blockchains use qubic?
    13.  /team - who are the team members of Qubic blockchain? 
    14. /whyUPoW - why UPow?
    15. /UPoW -  what is  Useful Proof of Work?
    16. /oracles - oracles
    17. /whyQubic - what's new about Qubic blockchain?
    18. /gpuMining - can i use gpu to mine?
    19. /cpuMining - mining Qubic coins with Cpu
    20. /transactionTimeout - what happens when my transaction fails?
    21. /createQubicWallet -how to create a wallet
    22. /manageSeed - how to manage your seed
    23. /CSupply - to check the circulating supply]
    24. /Mcap to check the marketcap
    25. /maxSupply - to check the maximum supply
    26. /price - to check the price of Qubic
    27. /fdv - to check Qubic's fully diluted valuation
    
    """
    await update.message.reply_text(message)
    ""



async def echo(update):
    
    await update.message.reply_text(update.message.text)


def main():
    app = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()

    #commands you can call 
    commands = {
    "start": start,
    "otc": otc,
    "AI": AI,
    "founder": founder,
    "history": history,
    "whitepaper": whitepaper,
    "docs": docs,
    "help": help,
    "node": node,
    "arbitor": arbitor,
    "aigarth": aigarth,
    "algorithm": algorithm,
    "qubicBlockchain": qubicBlockchain,
    "team": team,
    "whyUPoW": whyUPoW,
    "UPoW": UPoW,
    "oracles": oracles,
    "whyQubic": whyQubic,
    "gpuMining": gpuMining,
    "cpuMining": cpuMining,
    "transactionTimeout": transactionTimeout,
    "createQubicWallet": createQubicWallet,
    "manageSeed": manageSeed,
    # "totalSupply": totalSupply,
    # "Mcap": Mcap,
    "maxSupply": maxSupply,
    "price": price,
    "fdv": fdv,
}

    for command in commands:
        func = globals().get(command)
        if func:
            app.add_handler(CommandHandler(command, func))
    else:
        print(f"No function matches the command: {command}")
    


    # app.add_handler(Application.remove_handler(filters.Text & ~filters.Command, echo))

    app.run_polling(3, allowed_updates=Update.ALL_TYPES)
    # app.run_polling(allowed_updates=["message"])

if __name__ == "__main__":
    main()
