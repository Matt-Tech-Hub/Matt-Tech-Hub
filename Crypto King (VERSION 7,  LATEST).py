# import libraries
import random


# INITIALISE global variables and define functions that will be called in weeks 1-6
# GLOBAL VARIABLES
crypto = 0
amount = 0
multiplier = 0
gains = 0
sell = 0
name = input("What is your name? ")
game = "Crypto King"
title_ascii = """
                                     $$$$$$\  $$$$$$$\  $$\     $$\ $$$$$$$\  $$$$$$$$\  $$$$$$\  
                                    $$  __$$\ $$  __$$\ \$$\   $$  |$$  __$$\ \__$$  __|$$  __$$\ 
                                    $$ /  \__|$$ |  $$ | \$$\ $$  / $$ |  $$ |   $$ |   $$ /  $$ |
                                    $$ |      $$$$$$$  |  \$$$$  /  $$$$$$$  |   $$ |   $$ |  $$ |
                                    $$ |      $$  __$$<    \$$  /   $$  ____/    $$ |   $$ |  $$ |
                                    $$ |  $$\ $$ |  $$ |    $$ |    $$ |         $$ |   $$ |  $$ |
                                    \$$$$$$  |$$ |  $$ |    $$ |    $$ |         $$ |    $$$$$$  |
                                     \______/ \__|  \__|    \__|    \__|         \__|    \______/ 
                                    
                                    
                                    
                                      $$\   $$\       $$$$$$\       $$\   $$\        $$$$$$\        
                                      $$ | $$  |      \_$$  _|      $$$\  $$ |      $$  __$$\       
                                      $$ |$$  /         $$ |        $$$$\ $$ |      $$ /  \__|      
                                      $$$$$  /          $$ |        $$ $$\$$ |      $$ |$$$$\       
                                      $$  $$<           $$ |        $$ \$$$$ |      $$ |\_$$ |      
                                      $$ |\$$\          $$ |        $$ |\$$$ |      $$ |  $$ |      
                                      $$ | \$$\       $$$$$$\       $$ | \$$ |      \$$$$$$  |      
                                      \__|  \__|      \______|      \__|  \__|       \______/       
"""


liquidated_ascii = """
                                                  $$\     $$\                 $$\                            $$\                                                                
                                                  \$$\   $$  |                $  |                           $$ |                                                               
                                                   \$$\ $$  /$$$$$$\  $$\   $$\\_/$$\    $$\  $$$$$$\         $$$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\                             
                                                    \$$$$  /$$  __$$\ $$ |  $$ |  \$$\  $$  |$$  __$$\       $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\                            
                                                     \$$  / $$ /  $$ |$$ |  $$ |   \$$\$$  / $$$$$$$$ |      $$ |  $$ |$$$$$$$$ |$$$$$$$$ |$$ |  $$ |                           
                                                      $$ |  $$ |  $$ |$$ |  $$ |    \$$$  /  $$   ____|      $$ |  $$ |$$   ____|$$   ____|$$ |  $$ |                           
                                                      $$ |  \$$$$$$  |\$$$$$$  |     \$  /   \$$$$$$$\       $$$$$$$  |\$$$$$$$\ \$$$$$$$\ $$ |  $$ |                           
                                                      \__|   \______/  \______/       \_/     \_______|      \_______/  \_______| \_______|\__|  \__|                           
                                                                                                                                                                                
                                                                                                                                                                                
                                                                                                                                                                                
                          $$\             $$$$$$\        $$$$$$\        $$\   $$\       $$$$$$\       $$$$$$$\         $$$$$$\        $$$$$$$$\       $$$$$$$$\       $$$$$$$\  
                          $$ |            \_$$  _|      $$  __$$\       $$ |  $$ |      \_$$  _|      $$  __$$\       $$  __$$\       \__$$  __|      $$  _____|      $$  __$$\ 
                          $$ |              $$ |        $$ /  $$ |      $$ |  $$ |        $$ |        $$ |  $$ |      $$ /  $$ |         $$ |         $$ |            $$ |  $$ |
                          $$ |              $$ |        $$ |  $$ |      $$ |  $$ |        $$ |        $$ |  $$ |      $$$$$$$$ |         $$ |         $$$$$\          $$ |  $$ |
                          $$ |              $$ |        $$ |  $$ |      $$ |  $$ |        $$ |        $$ |  $$ |      $$  __$$ |         $$ |         $$  __|         $$ |  $$ |
                          $$ |              $$ |        $$ $$\$$ |      $$ |  $$ |        $$ |        $$ |  $$ |      $$ |  $$ |         $$ |         $$ |            $$ |  $$ |
                          $$$$$$$$\       $$$$$$\       \$$$$$$ /       \$$$$$$  |      $$$$$$\       $$$$$$$  |      $$ |  $$ |         $$ |         $$$$$$$$\       $$$$$$$  |
                          \________|      \______|       \___$$$\        \______/       \______|      \_______/       \__|  \__|         \__|         \________|      \_______/ 
                                                             \___|                                                                                                              
"""

# FUNCTIONS
# HOLDING FEE FUNCTION

# BUYING FUNCTION


def buy_crypto():
    global crypto
    global amount
    amount = int(input(
        "How much would you like to buy? \n (Enter amount...) "))
    if amount > crypto:
        input(
            "You do not have enough money to make that purchase. \n (Press enter to continue)")
        input("The bank suspects you of fraud and you assets have been frozen. \n (Press enter to continue)")
        amount = 0
        crypto -= crypto
        liquidated()
    crypto -= amount


def holding_fee():
    global crypto
    crypto -= 250
    return crypto

# GAME OVER FUNCTION FOR EACH WEEK


def liquidated():
    global crypto
    if crypto <= 0:
        print(liquidated_ascii)
        input("You lost all of your assets. (press enter) ")
        input("Continue? press enter ")
        amount = 0
        crypto = 500
        return amount, crypto


# INVESTMENT GOES UP (call this function when the user wins and their amount invested * x amount)


def investment_up():
    global multiplier
    global amount
    global crypto
    global gains

    multiplier = random.randint(2, 5)
    gains = amount
    gains *= multiplier
    crypto += gains

    return int(multiplier), int(gains)

# INVESTMENT GOES DOWN (call this function when the user wins and their amount invested / x amount)


def investment_down():
    global multiplier
    global amount
    global crypto
    global gains

    multiplier = random.randint(2, 5)
    gains = amount
    gains /= multiplier
    crypto += gains

    return int(multiplier), int(gains)

# mystery_crypto function if the number is even, your winnings are mulipied by 10-20


def mystery_crypto():
    global crypto
    randnum = random.randint(1, 100)
    if randnum % 2 == 0:
        crypto *= random.randint(10, 20)
    else:
        crypto = 0


#
#
#
#
################## INTRO  #####################
#
#
#
#


def intro():
    global crypto
    global name
    input(f"Hello {name}, welcome to {game}, the game where you become a new investor in the world of crypto. \n (Press enter to continue)")
    input("Each week you will receive a different investment scenario that you will have to navigate. Should you take the opportunity and invest, sell your investments, or hold off until a new opportunity arises? \n (Press enter to continue)")
    input("Your decisions will determine the success of your investments and ultimately, your financial future. \n (Press enter to continue)")
    input("Here's $1000 in crypto to get started. \n (Press enter to continue)")
    input("If you lose you can choose to continue but your investments will be taken and your balance will be reset to $500! \n (Press enter to continue)")
    crypto += 1000
    input(f"Good luck! You have ${crypto}. \n (Press enter to continue)")
    print(title_ascii)
    liquidated()


# call intro function
intro()

#
#
#
#
################## WEEK 1 #####################
#
#
#
#


# week_1_buy (option b)

def week_1_buy():
    global crypto
    global amount
    global multiplier
    global gains
    buy_crypto()
    input("Good news! The market is up. \n (Press enter to continue)")
    investment_up()
    input(
        f"Your investment of ${amount} went up by times {multiplier}! \n (Press enter to continue)")
    input(f"You have ${crypto} remaining. \n (Press enter to continue)")
    liquidated()  # call the liquidated function
# week_1_hold (option h)


def week_1_hold():
    global crypto
    input("You chose to hold your investment! \n (Press enter to continue)")
    input("There is a holding fee $250 worth charge per week to hold. \n (Press enter to continue)")
    holding_fee()
    input(f"You have {crypto} remaining \n (Press enter to continue)")
    liquidated()  # call the liquidated function

# WEEK_1_MAIN


def week_1():
    global crypto
    input("Week 1! \n (Press enter to continue)")
    input("Investment opportunity!")
    input("You're at home, browsing the internet. As you scroll through your social media feed, you notice an article about a new investment opportunty. \n (Press enter to continue)")
    input("'BTC Reclaims $28K After Enhanced Volatility': Market Watch \n (Press enter to continue)'")
    input(f"You have ${crypto} \n (Press enter to continue)")
    week_1_ans = input(
        "What do you do? Buy or hold? (Press 'B' to buy or 'H' to hold) ").lower()
    if week_1_ans == "b":
        week_1_buy()
    elif week_1_ans == "h":
        week_1_hold()
    else:
        input("Wrong input")
        week_1()


week_1()

#
#
#
#
################## WEEK 2 #####################
#
#
#
#


# week_2_buy (option b)

def week_2_buy():
    global crypto
    global amount

    buy_crypto()
    crypto += amount
    input("The market is flat! Your balance stays the same. \n (Press enter to continue)")
    input(
        f"Your investment of {amount} stays the same.\n (Press enter to continue)")
    input(f"You have {crypto} in your wallet. \n (Press enter to continue)")
    liquidated()


# week_2_hold (option h)

def week_2_hold():
    global crypto
    input("You chose to hold your investment! \n (Press enter to continue)")
    input("There is a holding fee $250 worth charge per week to hold. \n (Pressenter to continue)")
    holding_fee()
    input(f"You have {crypto} remaining. \n (Press enter to continue)")
    liquidated()


# week_2_sell (option s)

def week_2_sell():
    global crypto
    input("You chose to sell your investment! \n (Press enter to continue)")
    input("Your crypto amount stays the same. \n (Pressenter to continue)")
    input(f"You have {crypto} in your wallet. \n (Press enter to continue)")
    liquidated()

# WEEK 2 MAIN


def week_2():
    global crypto
    input("Week 2! \n (Press enter to continue)")
    input("Another investment opportunity is here!")
    input("You're feeling great and you want to capitalise on your success. You hear a rumour that:\n (Press enter to continue)")
    input("'Denmark to Start Taxing Bitcoin Profits, Rules the Supreme Court. \n (Press enter to continue)'")
    input(f"You have ${crypto}. \n (Press enter to continue)")
    week_2_ans = input(
        "What do you do? Buy or hold or sell? (Press 'b' to buy, 'h' to hold, 's' to sell) ").lower()
    if week_2_ans == "b":
        week_2_buy()
    elif week_2_ans == "h":
        week_2_hold()
    elif week_2_ans == "s":
        week_2_sell()
    else:
        input("Wrong input")
        week_2()


week_2()

input(f"You now have {crypto} left to invest. \n (Press enter to continue)")


#
#
#
#
################## WEEK 3 #####################
#
#
#
#

# WEEK_3_BUY
def week_3_buy():
    global crypto
    global amount
    global multiplier
    global gains
    buy_crypto()
    input("Good news! The market is up. \n (Press enter to continue)")
    investment_up()
    input(
        f"Your investment of {amount} went up by times {multiplier}! \n (Press enter to continue)")
    input(f"You have {crypto} remaining. \n (Press enter to continue)")
    liquidated()

# WEEK_3_SELL


def week_3_sell():
    global crypto
    global amount
    global multiplier
    global gains
    global sell
    sell = int(input(
        "How much would you like to sell? \n (Enter amount...) "))
    input("Bad news! The market is up. You could have made a lot of money! \n (Press enter to continue)")
    input(f"You have ${crypto} remaining. \n (Press enter to continue)")
    liquidated()

# WEEK_3_HOLD


def week_3_hold():
    global crypto
    input("You chose to hold your investment! \n (Press enter to continue)")
    input("There is a holding fee $250 worth charge per week to hold. \n (Press enter to continue)")
    holding_fee()
    crypto -= crypto
    input(
        f"devastating news! Silicon Valley Bank has collapsed! You lost all of your assets! You have {crypto} remaining. \n (Press enter to continue)")
    liquidated()


# WEEK_3_MAIN

def week_3_main():
    global crypto
    input("Week 3! \n (Press enter to continue)")
    input("This week's News! \n (Press enter to continue)")
    input("'Big Shorts Michael Burry Says He “Was Wrong to Say Sell” \n (Press enter to continue)'")
    input(f"You have ${crypto}. \n (Press enter to continue)")
    week_1_ans = input(
        "What do you do? Buy, sell or hold? (Press 'B' to buy, 'S' to sell or 'H' to hold) ").lower()
    if week_1_ans == "b":
        week_3_buy()
    elif week_1_ans == "s":
        week_3_sell()
    elif week_1_ans == "h":
        week_3_hold()
    else:
        input("Wrong input")
        week_3_main()


week_3_main()


#
#
#
#
################## WEEK 4 #####################
#
#
#
#

# week_MAIN_4

# WEEK 4 BUY
def week_4_buy():
    global crypto
    global amount
    global multiplier
    global gains
    buy_crypto()
    input("Bad News! The market crashed. \n (Press enter to continue)")
    crypto -= crypto
    input(
        f"The market doesn't always go the way we want. It is more like an ocean, it is always calm before the storm. Unfortunately, your boat has sunk. Your investment has been liquidated. \n (Press enter to continue)")
    input(f"You have ${crypto} remaining \n (Press enter to continue)")
    liquidated()

# WEEK 4 SELL


def week_4_sell():
    global crypto
    global amount
    global multiplier
    amount = int(input(
        "How much would you like to sell? \n (Enter amount...) "))
    crypto += 250
    input("Good news! The market went down but you decided to sell. You've made $250. \n (Press enter to continue)")
    input(f"You have ${crypto} remaining. \n (Press enter to continue)")
    liquidated()

# WEEK 4 HOLD


def week_4_hold():
    global crypto
    input("You chose to hold your investment! \n (Press enter to continue)")
    input("There is a holding fee $250 worth charge per week to hold. \n (Press enter to continue)")
    holding_fee()
    crypto = 0
    input(
        f"devastating news! Silicon Valley Bank has collapsed! You lost all of your assets! You have {crypto} remaining \n (Press enter to continue)")
    liquidated()


def week_4_main():
    global crypto
    input("Week 4! \n (Press enter to continue)")
    input("This week's News! \n (Press enter to continue)")
    input("'Gary Gensler, the chairman of the SEC wants more SEC Funding to Crack Down on Wild West Crypto.” \n (Press enter to continue)'")
    input(f"You have ${crypto} \n (Press enter to continue)")
    week_1_ans = input(
        "What do you do? Buy, sell or hold? (Press 'B' to buy, 'S' to sell or 'H' to hold) ").lower()
    if week_1_ans == "b":
        week_4_buy()
    elif week_1_ans == "s":
        week_4_sell()
    elif week_1_ans == "h":
        week_4_hold()
    else:
        input("Wrong input")
        week_4_main()


week_4_main()


#
#
#
#
################## WEEK 5 #####################
#
#
#
#


# SELL FUNCTION + ADD $250

def week_5_sell():
    global crypto
    global amount
    global multiplier
    amount = int(input(
        "How much would you like to sell? \n (Enter amount...) "))
    crypto += 250
    crypto = int(crypto)
    input("Congrats! You have received a trading bonus of $250. \n (Press enter to continue)")
    input(f"You have ${crypto} remaining. \n (Press enter to continue)")


# week_5_buy (option b)

def week_5_buy():
    global crypto
    global amount
    global multiplier
    buy_crypto()
    input("Bad luck! The market is down. \n (Press enter to continue)")
    investment_down()
    input(
        f"Your investment of {amount} decreased by {multiplier} fold! \n (Press enter to continue)")
    input(f"You have ${crypto} remaining \n (Press enter to continue)")


# week_5_hold (option h)

def week_5_hold():
    global crypto
    input("You chose to hold your investment! \n (Press enter to continue)")
    input("There is a holding fee $250 worth charge per week to hold \n (Press enter to continue)")
    holding_fee()
    input(f"You have ${crypto} remaining. \n (Press enter to continue)")


# WEEK_5_MAIN
def week_5():
    global crypto
    input("Week 5! \n (Press enter to continue)")
    input("Investment opportunity!")
    input("You're out on a walk when your phone buzzes in your pocket. You check your phone to see a notification from BBC news. \n (Press enter to continue)")
    input("These Brazilian Soccer Players Became Victims of a Crypto Scam. (Report) \n (Press enter to continue)'")
    input(f"You have ${crypto} \n (Press enter to continue)")
    week_5_ans = input(
        "What do you do? Buy, sell or hold? (Press 'b' to buy, 's' to sell or 'h' to hold) ").lower()
    if week_5_ans == "b":
        week_5_buy()
    elif week_5_ans == "h":
        week_5_hold()
    elif week_5_ans == "s":
        week_5_sell()
    else:
        input("Wrong input")
        week_5()


week_5()


#
#
#
#
################## WEEK 6 #####################
#
#
#
#


# Buy option for week 6 (b)
def week_6_buy():
    global crypto
    global amount
    global multiplier
    global gains
    buy_crypto()
    input("Good news! The market is up. \n (Press enter to continue)")
    investment_up()
    input(
        f"Your investment of {amount} went up by times {multiplier}! \n (Press enter to continue)")
    input(f"You have {crypto} remaining \n (Press enter to continue)")


# Hold option for week 6 (h)

def week_6_hold():
    global crypto
    input("You chose to hold your investment! \n (Press enter to continue)")
    input("There is a holding fee $250 worth charge per week to hold. \n (Press enter to continue)")
    holding_fee()
    input(f"You have {crypto} remaining \n (Press enter to continue)")


# The main branch for week 6
def week_6():
    global crypto
    input("Investment opportunity!")
    input("On your way home from work, you pop into the newsagent for your usual sundries. Out of the corner of your eye, you see the headlines for Finance Weekly. \n (Press enter to continue)")
    input("3 Reasons Ripple is Up 60% in the Past 10 Days \n (Press enter to continue)")
    input(f"You have ${crypto} \n (Press enter to continue)")
    week_6_ans = input(
        "What do you do? Buy, sell or hold? (Press 'b' to buy, 'h' to hold, or 's' to sell) ").lower()
    if week_6_ans == "b":
        week_6_buy()
    elif week_6_ans == "h":
        week_6_hold()
    elif week_6_ans == "s":
        print("You choose to play it safe. Your balance remains the same. \n (Press enter to continue)")
    else:
        input("Wrong input")
        week_6()
    liquidated()


week_6()


#
#
#
#
################## END #####################
#
#
#
#


def ending():
    input("Success! Your business acumen did not let you down! \n (Press enter)")
    input("Do you want to end your investing journey here or risk it all to win big? \n (Press enter)")
    end_ans = input(
        " Would you like to invest all your money in the mystery Crypto?  \n (Press 'Y' to invest or 'N' to ignore)").lower()
    if end_ans == "y":
        mystery_crypto()


ending()


#
#
#
#
################## SCORING #####################
#
#
#
#

ascii_thanks = """
$$$$$$$$\ $$\                           $$\                        $$$$$$\                                      $$\                     $$\                     $$\ 
\__$$  __|$$ |                          $$ |                      $$  __$$\                                     $$ |                    \__|                    $$ |
   $$ |   $$$$$$$\   $$$$$$\  $$$$$$$\  $$ |  $$\  $$$$$$$\       $$ /  \__| $$$$$$\   $$$$$$\         $$$$$$\  $$ | $$$$$$\  $$\   $$\ $$\ $$$$$$$\   $$$$$$\  $$ |
   $$ |   $$  __$$\  \____$$\ $$  __$$\ $$ | $$  |$$  _____|      $$$$\     $$  __$$\ $$  __$$\       $$  __$$\ $$ | \____$$\ $$ |  $$ |$$ |$$  __$$\ $$  __$$\ $$ |
   $$ |   $$ |  $$ | $$$$$$$ |$$ |  $$ |$$$$$$  / \$$$$$$\        $$  _|    $$ /  $$ |$$ |  \__|      $$ /  $$ |$$ | $$$$$$$ |$$ |  $$ |$$ |$$ |  $$ |$$ /  $$ |\__|
   $$ |   $$ |  $$ |$$  __$$ |$$ |  $$ |$$  _$$<   \____$$\       $$ |      $$ |  $$ |$$ |            $$ |  $$ |$$ |$$  __$$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |    
   $$ |   $$ |  $$ |\$$$$$$$ |$$ |  $$ |$$ | \$$\ $$$$$$$  |      $$ |      \$$$$$$  |$$ |            $$$$$$$  |$$ |\$$$$$$$ |\$$$$$$$ |$$ |$$ |  $$ |\$$$$$$$ |$$\ 
   \__|   \__|  \__| \_______|\__|  \__|\__|  \__|\_______/       \__|       \______/ \__|            $$  ____/ \__| \_______| \____$$ |\__|\__|  \__| \____$$ |\__|
                                                                                                      $$ |                    $$\   $$ |              $$\   $$ |    
                                                                                                      $$ |                    \$$$$$$  |              \$$$$$$  |    
                                                                                                      \__|                     \______/                \______/     
"""
ascii_cake = """
                                                                                                    
                                                                                                    
                                             &&&&&(.*%&&&&                                          
                                          &&              %&&                                      
                                        &&                *&                                 
                                       &#              &&                                         
                                      &&              .&                                            
                                      &%               &&                                           
                                      *&                 &&                                         
                                     &&(&                   .&&&                                    
                                   &&    *&                    __#&&                                
                                  &         ```---------- `````      &&                             
                              *&&&.                                   (&&&                          
                         &&#     &&                                   &   &                      
                       &&          &&                               &(    &&                   
                      ,&              /&&%__            _____&&*````        *&                   
                   __/#&                    **¬¬¬¬¬¬****                      &                   
               &&&    &&                                                       *&                   
             &.          &                                                     && *&&&              
           &&              &&                                                (&        &%           
          *&                  *&&/__                                      &&(            &          
          &%                        \&&&&(```----,,       ,,,---¬¬¬¬¬/&&&&,               &         
           &                                       ```````                                &         
        _.&&&                                                                            &&         
     %&,     &&                                                                         &*  #&(    
   &&           &&                                                                   /&,       &.  
  &&               ,&&,__                                                       __&&            &,
  &                      &&&%___                                         ___&&&(                 & 
  &&                            .&&&&&&%,```,,,          ,,,````,#&&&&&&(                        &) 
   &&                                         -----------                                       &&  
     &%                                                                                       &&    
      &&&%                                                                                 &&&*     
       &,  &&&                                                                         &&%  &&      
        &      & &&&&,                                                         *&&&& *      &       
        *&      &         (&&&&&&&%(.¬¬¬*********---***********¬¬.%&&&&&&&&*         &      &        
         &%     ,           ,          %          &          &          %          ,      &%        
          &      &          &          &          &          &          &          &     /&         
           &      .         /          &          &          %         .          &      &          
           %&     &          %         (          &                    &          #     &.          
            &/     &         &          .         &         %          #         &     &&           
             &     #                    #         &         &         #                &            
             .&     &         &         &         &         &         &         &     &             
              &&     .        #         &         &         %                  %     &/             
               &     &         &        (         &                  &         &    %&              
                &     #        &                  &        (         %        &     &               
                (&    %                  #        &        &        #              &                
                 &%    &        &        &        &        &        &        &    &&                
                  &    .        &        &        &        %        .       /    ,&                 
                   &    &        (       #        &                &        &    &                  
                     %&& /       &       .        &       /        &       & &&,                    
                          %&&%            #       &       &       /    &&&(                         
                              ****&&&&&/***&       &       &****(&&&&%*                               
                                           **************** 

                 $$$$$$\                      $$$$$$$$\ $$\                     
                $$  __$$\                     \__$$  __|\__|                    
                $$ /  \__|                       $$ |   $$\  $$$$$$\   $$$$$$\  
                \$$$$$$\        $$$$$$\          $$ |   $$ |$$  __$$\ $$  __$$\ 
                 \____$$\       \______|         $$ |   $$ |$$$$$$$$ |$$ |  \__|
                $$\   $$ |                       $$ |   $$ |$$   ____|$$ |      
                \$$$$$$  |                       $$ |   $$ |\$$$$$$$\ $$ |      
                 \______/                        \__|   \__| \_______|\__|        
"""
rating_f = """
                $$$$$$$$\                     $$$$$$$$\ $$\                     
                $$  _____|                    \__$$  __|\__|                    
                $$ |                             $$ |   $$\  $$$$$$\   $$$$$$\  
                $$$$$\          $$$$$$\          $$ |   $$ |$$  __$$\ $$  __$$\ 
                $$  __|         \______|         $$ |   $$ |$$$$$$$$ |$$ |  \__|
                $$ |                             $$ |   $$ |$$   ____|$$ |      
                $$ |                             $$ |   $$ |\$$$$$$$\ $$ |      
                \__|                             \__|   \__| \_______|\__|      
"""
rating_d = """
                $$$$$$$\                      $$$$$$$$\ $$\                     
                $$  __$$\                     \__$$  __|\__|                    
                $$ |  $$ |                       $$ |   $$\  $$$$$$\   $$$$$$\  
                $$ |  $$ |      $$$$$$\          $$ |   $$ |$$  __$$\ $$  __$$\ 
                $$ |  $$ |      \______|         $$ |   $$ |$$$$$$$$ |$$ |  \__|
                $$ |  $$ |                       $$ |   $$ |$$   ____|$$ |      
                $$$$$$$  |                       $$ |   $$ |\$$$$$$$\ $$ |      
                \_______/                        \__|   \__| \_______|\__|      
"""
rating_c = """
                 $$$$$$\                      $$$$$$$$\ $$\                     
                $$  __$$\                     \__$$  __|\__|                    
                $$ /  \__|                       $$ |   $$\  $$$$$$\   $$$$$$\  
                $$ |            $$$$$$\          $$ |   $$ |$$  __$$\ $$  __$$\ 
                $$ |            \______|         $$ |   $$ |$$$$$$$$ |$$ |  \__|
                $$ |  $$\                        $$ |   $$ |$$   ____|$$ |      
                \$$$$$$  |                       $$ |   $$ |\$$$$$$$\ $$ |      
                 \______/                        \__|   \__| \_______|\__|      
"""
rating_b = """
                $$$$$$$\                      $$$$$$$$\ $$\                     
                $$  __$$\                     \__$$  __|\__|                    
                $$ |  $$ |                       $$ |   $$\  $$$$$$\   $$$$$$\  
                $$$$$$$\ |      $$$$$$\          $$ |   $$ |$$  __$$\ $$  __$$\ 
                $$  __$$\       \______|         $$ |   $$ |$$$$$$$$ |$$ |  \__|
                $$ |  $$ |                       $$ |   $$ |$$   ____|$$ |      
                $$$$$$$  |                       $$ |   $$ |\$$$$$$$\ $$ |      
                \_______/                        \__|   \__| \_______|\__|      
"""

rating_a = """
                 $$$$$$\                      $$$$$$$$\ $$\                     
                $$  __$$\                     \__$$  __|\__|                    
                $$ /  $$ |                       $$ |   $$\  $$$$$$\   $$$$$$\  
                $$$$$$$$ |      $$$$$$\          $$ |   $$ |$$  __$$\ $$  __$$\ 
                $$  __$$ |      \______|         $$ |   $$ |$$$$$$$$ |$$ |  \__|
                $$ |  $$ |                       $$ |   $$ |$$   ____|$$ |      
                $$ |  $$ |                       $$ |   $$ |\$$$$$$$\ $$ |      
                \__|  \__|                       \__|   \__| \_______|\__|      
"""
# these variables are just for test purposes (they should match the functions in the main game)


def score_rating():
    global crypto
    if crypto == 0:
        input(
            f"You ended with {crypto} amount of crypto in your wallet.\n (Press enter)")
        # f rating
        input("You went big but unfortunately you fell flat!\n (Press enter)")
        print(rating_f)
    elif crypto in range(1, 999):
        input(
            f"You ended with {crypto} amount of crypto in your wallet.\n (Press enter)")
        print(rating_f)
        input("Maybe you're just not cut out for this...\n (Press enter)")  # f rating
    elif crypto in range(1000, 1999):
        input(
            f"You ended with {crypto} amount of crypto in your wallet.\n (Press enter)")
        print(rating_d)
        input("At least you broke even\n (Press enter)")  # d rating
    elif crypto in range(2000, 3999):
        input(
            f"You ended with {crypto} amount of crypto in your wallet.\n (Press enter)")
        print(rating_c)
        input("A great start... for now at least!\n (Press enter)")  # c rating
    elif crypto in range(4000, 5999):
        input(
            f"You ended with {crypto} amount of crypto in your wallet.\n (Press enter)")
        print(rating_b)
        input("Very nice!\n (Press enter)")  # b rating
    elif crypto in range(6000, 7999):
        input(
            f"You ended with {crypto} amount of crypto in your wallet.\n (Press enter)")
        print(rating_a)
        input("Now that's epic!\n (Press enter)")  # a rating
    elif crypto in range(8000, 1000000):
        input(
            f"You ended with {crypto} amount of crypto in your wallet.\n (Press enter)")
        print(ascii_cake)
        # else covers any 8000+ score (s rating)
        input(
            f"Cake is for true winners. Eat to your heart's content, {name}!\n (Press enter)")


score_rating()
print(ascii_thanks)
