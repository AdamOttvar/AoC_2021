import subprocess
import lib.AoC_lib as AoC

finished_days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']

@AoC.timer
def run_all_days(finished_days):
    for day in finished_days:
        subprocess.call(['python', 'day' + day + '.py'])

    print('')
    print('Total time for all days: ')


if __name__ == '__main__':
    run_all_days(finished_days)