"""Elo Calculations
Chris Snyder Oct30

# Python 3 program for Elo Rating, Nurse Hemolysis Project

initial code fork from: https://www.geeksforgeeks.org/elo-rating-algorithm/

Elo Example:

Suppose there is a live match on chess.com between two players 
rating1 = 1200, rating2 = 1000; 
P1 = (1.0 / (1.0 + pow(10, ((1000-1200) / 400)))) = 0.76 
P2 = (1.0 / (1.0 + pow(10, ((1200-1000) / 400)))) = 0.24 
  And Assume constant K=30; 
  CASE-1 : 
  Suppose Player 1 wins: rating1 = rating1 + k*(actual – expected) = 1200+30(1 – 0.76) = 1207.2; 
  rating2 = rating2 + k*(actual – expected) = 1000+30(0 – 0.24) = 992.8; 
  Case-2 : 
  Suppose Player 2 wins: rating1 = rating1 + k*(actual – expected) = 1200+30(0 – 0.76) = 1177.2; 
  rating2 = rating2 + k*(actual – expected) = 1000+30(1 – 0.24) = 1022.8;
"""

SCALE_FACTOR=400.
NOOB_RATING=800#day 1
K_FACTOR=24#hyperparamter scales with maximum elo change per paircomparison

class Nurse():
    """_summary_
    """
    round=1
    def __init__(self,elo=NOOB_RATING,**kwargs ):
        """_summary_

        Args:
            elo (_type_, optional): _description_. Defaults to NOOB_RATING.
        """
        
        self.info=kwargs #floor, years_as_nurse, service etc.
        self.elo = elo


def Probability(victor,defeats):
    nurse2=victor
    nurse1=defeats
    _frac = lambda x : 1./(1.+x)#dataframe safe
    _exp  = lambda y : 10**y
    prob= _frac(
                _exp( 
                     (nurse2.elo-nurse1.elo)/SCALE_FACTOR 
                     )
                 )
    
    return prob

def update_rating(victor, defeats):
    """_summary_

    Args:
        victor (_type_): _description_
        defeats (_type_): _description_
    """
    N2=victor
    N1=defeats

    # To calculate the Winning
    # Probability of Player 2
    P2 = Probability(N2,defeats=N1)
 
    # To calculate the Winning
    # Probability of Player 1
    P1 = Probability(N1, defeats=N2)
 
    # Case When Player 2 wins
    # Updating the Elo Ratings
    N2.elo += K_FACTOR * (1. - P2)
    N1.elo += K_FACTOR * (0. - P1)
    
    


 if __name__=='__main__':
    #
    sally=Nurse()
    arnold=Nurse()
    
    #assume N2 "wins" round 1
    Nurse.round+=1
    update_rating(  sally, defeats=arnold  )

    with_likelihood( Probability(  ))
    # Ra and Rb are current ELO ratings
    Ra = 1200
    Rb = 1000
    K = 30
    d = 1
    EloRating(Ra, Rb, K, d)

