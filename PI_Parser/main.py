"""
Simply checks if epic_pmrn and other values are not null from mgbedw_parser_patientidentifiers
 and parses them to mgbedw_patientidentifiers

Authored by Jon Dong 9/2/2021
"""

import sys
import os
from connectionmethods import connect_to_postgres, connect_to_rabbitmq
from dbmethods import insert_row_into_parsed_patientidentifiers,grab_info_from_mgbdew_patientidentifiers

def process_pt_identifiers(input_epicpmrn, inputempi, input_bwh, inputmgh):
    """
    Checks if any Values are null
    :param input_epicpmrn: epic pmrn
    :param inputempi: empi
    :param input_bwh: bwh id
    :param inputmgh: mgh id
    :return: epicpmrn, empi, bwh if all are not null, else returns None

    """
    if(input_epicpmrn,inputempi,input_bwh,inputmgh is not None):
        return (input_epicpmrn,inputempi,input_bwh,inputmgh)
    else:
        return None

def main():
    #connect to db
    postgrescon, postgrescur = connect_to_postgres()
    rabbitconnection, rabbitchannel = connect_to_rabbitmq()



    def callback(ch, method, properties, body):
        try:
            #error check that message from rabbitmq queue is int
            IDasint = int(body)

            input_epic, input_empi, input_bwh, input_mgh = grab_info_from_mgbdew_patientidentifiers(IDasint,postgrescur,postgrescon)
            if (process_pt_identifiers(input_epic, input_empi,input_bwh, input_mgh) is not None):
                insert_row_into_parsed_patientidentifiers(process_pt_identifiers())
                ch.basic_ack(delivery_tag=method.delivery_tag)
            else:
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

        except ValueError:
            print("Error, rowid not int")
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
            return

    print(' [*] Waiting for messages. To exit press CTRL+C')
    rabbitchannel.basic_consume(queue=os.getenv("ROWIDQUEUE"), on_message_callback=callback, auto_ack=False)

    rabbitchannel.start_consuming()

if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)


