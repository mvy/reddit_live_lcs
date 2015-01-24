from models import team, lineup, match
import supervisor, copy

def setupTestDefaults():
    m_ = supervisor.Supervisor.match()

    t_ = team.Team()
    t_.populate("Test", "TST", "j1", "j2", "j3", "j4", "j5")
    m_.set_blue_team(copy.deepcopy(t_))
    t_.populate("Test2", "TST2", "j12", "j22", "j32", "j42", "j52")
    m_.set_purple_team(copy.deepcopy(t_))
    l_ = lineup.Lineup()
    l_.set_list(['Ahri', 'Braum', 'Caitlin', 'Draven', 'Evelynn', 'Fizz',
                'Gragas', 'Hecarim', 'Irelia', 'Jarvan IV'])
    m_.set_lineup(l_)
