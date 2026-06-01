#include QMK_KEYBOARD_H
#include "raw_hid.h"

enum layers {
    BASE,
    FN
};

enum custom_keycodes {
    OLED_TOGGLE = SAFE_RANGE
};

static uint8_t oled_mode = 0;

static char current_time[16] = "Waiting...";
static char current_date[32] = "No Date";

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    if (!record->event.pressed) return true;

    switch (keycode) {
        case OLED_TOGGLE:
            oled_mode = (oled_mode + 1) % 3;
            return false;
    }

    return true;
}

/* RAW HID */
void raw_hid_receive(uint8_t *data, uint8_t length) {

    if (length < 2) return;

    switch (data[0]) {

        case 'T':
            strncpy(current_time, (char *)&data[1], sizeof(current_time) - 1);
            break;

        case 'D':
            strncpy(current_date, (char *)&data[1], sizeof(current_date) - 1);
            break;
    }
}

/* KEYMAP */
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

[BASE] = LAYOUT(
    MO(FN),
    KC_VOLU,
    KC_V,
    KC_C
),

[FN] = LAYOUT(
    KC_NO,
    KC_VOLD,
    OLED_TOGGLE,
    QK_BOOT
)
};

#ifdef OLED_ENABLE

oled_rotation_t oled_init_user(oled_rotation_t rotation) {
    return OLED_ROTATION_0;
}

bool oled_task_user(void) {

    oled_clear();

    switch (oled_mode) {

        case 0:
            oled_write_ln_P(PSTR("TIME"), false);
            oled_write_ln(current_time, false);
            break;

        case 1:
            oled_write_ln_P(PSTR("DATE"), false);
            oled_write_ln(current_date, false);
            break;

        case 2:
            oled_write_ln_P(PSTR("HELLO :)"), false);
            oled_write_ln_P(PSTR("Hack Club"), false);
            break;
    }

    return false;
}

#endif