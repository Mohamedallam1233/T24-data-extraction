from django.shortcuts import render
import paramiko
import time
import pandas as pd
import re
from io import StringIO
from django.http import HttpResponse

jump_host = '172.17.251.110'
jump_user = 't24'
jump_pass = 'KQJ@$foqv@74863'
# Commands to execute on the target servers

def run_commands_over_ssh(host, username, password, command):
    # Create an SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # Connect to the server
        client.connect(host, username=username, password=password, port=22)
        # Open a session
        channel = client.invoke_shell()
        channel.send("tRun tSS INTEL" + '\n')
        time.sleep(45)  # Add a delay to allow time for command execution
        # Wait for command execution to complete
        while not channel.recv_ready():
            time.sleep(10)
        channel.send(command+'\n')
        time.sleep(25)  # Add a delay to allow time for command execution
        # Wait for command execution to complete
        while not channel.recv_ready():
            time.sleep(10)

        output = channel.recv(4096).decode('utf-8')
        # print(output)
        return output
    except Exception as e:
        return False  # Return None for output and the error message
    finally:
        # Close the SSH connection
        client.close()

def convert_ofs_to_df(output , ofs_msg):

    data = output.split(ofs_msg)[1]
    data = data.split(",")
    columns = [re.sub(r'\W+', '', i.split("::")[1]) for i in data[1].split("/")]
    rows = [re.sub(r'"\s+"', '","', i).split('","')[0:] for i in data[2:]]
    print(columns)

    print("&&&&&&&&&&&&")
    print(rows)
    df = pd.DataFrame(rows, columns=columns)
    df.iloc[:, 0] = df.iloc[:, 0].str[1:]
    df.iloc[:, -1] = df.iloc[:, -1].str[:-1]


    return df


def index(request):
    # results = run_commands_over_ssh(jump_host, jump_user, jump_pass, commands_target)
    # print('*************************')
    # print(results)
    # convert_ofs_to_df(results)
    if request.method == 'POST':
        ofs_msg = request.POST.get('ofs_msg')
        print(ofs_msg)
        results = run_commands_over_ssh(jump_host, jump_user, jump_pass, ofs_msg)
        print('*************************')
        print(results)
        output_df = convert_ofs_to_df(results,ofs_msg)
        output = StringIO()
        output_df.to_csv(output, index=False)
        output.seek(0)
        # Prepare HTTP response for downloading the CSV file
        response = HttpResponse(output, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="t24ofsreport.csv"'
        return response


    return render(request, 'index.html')
