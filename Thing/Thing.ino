/*
 * Copyright (c) 2016, CESAR.
 * All rights reserved.
 *
 * This software may be modified and distributed under the terms
 * of the BSD license. See the LICENSE file for details.
 *
 */

/*
 * The default behavior for a Thing is to send data every 30 seconds.
 * To change its behavior on the firmware side, use the function
 * registerDefaultConfig(). See the documentation and lib examples.
 */

#include <KNoTThing.h>


#define LDR_PIN   A0
#define LDR_ID    2
#define LDR_NAME  "LDR"


KNoTThing thing;

static int ldr_read(int32_t *val, int32_t *multiplier)
{
    *val = analogRead(LDR_PIN);
    *multiplier = 1;
    Serial.print(F("LDR Value:"));
    Serial.println(*val);

    return 0;
}

static int ldr_write(int32_t *val,int32_t *multiplier){
    Serial.print(F("LDR Value:"));
    Serial.println(*val);
    return 0;  
}

void setup()
{
    Serial.begin(9600);


    pinMode(LDR_PIN,INPUT);
    /* TODO: Read lamp status from eeprom for reboot cases */
    thing.init("KGB Geo Bike");
    
    thing.registerIntData(LDR_NAME,LDR_ID, KNOT_TYPE_ID_LUMINOSITY,KNOT_UNIT_LUMINOSITY_LM,ldr_read,ldr_write);
    
    /* Send data every 10 seconds*/
    //thing.registerDefaultConfig(LIGHT_BULB_ID, KNOT_EVT_FLAG_TIME, 10, 0, 0, 0, 0);
    thing.registerDefaultConfig(LDR_ID, KNOT_EVT_FLAG_TIME, 10, 0, 0, 0, 0);

    Serial.println(F("LDR status"));
    int valo;
}


void loop()
{
    //Serial.println(analogRead(LDR_PIN));
    thing.run();
}
