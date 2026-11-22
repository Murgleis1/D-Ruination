"""The exit mat on the floor, not under it (user 2026-11-22: check everything back to Pelluca for inconsistencies).

Crown's rooms draw the door mat in the black row under the floor, and our first builds made that row the warp, so the
player arrived standing outside the room's outline. Base Emerald lays the mat on the floor's last row and makes that
row the warp (Littleroot, Oldale, Petalburg, Rustboro houses); MonoMyth makes the floor's last row the warp too, its
mat hanging over the floor's edge (its Chamomile Town houses, measured from its ROM). Mirroh's rooms follow Emerald.
"""
import numpy as np


def move_row(img, src_row, dst_row, x0=0, x1=None):
    """Lay a row's drawn pixels (everything not black: the mat) over another row, and black the row it leaves."""
    x1 = img.shape[1] // 16 if x1 is None else x1
    strip = img[src_row * 16:(src_row + 1) * 16, x0 * 16:x1 * 16].copy()
    m = strip.any(-1)
    dst = img[dst_row * 16:(dst_row + 1) * 16, x0 * 16:x1 * 16]
    dst[m] = strip[m]
    img[src_row * 16:(src_row + 1) * 16, x0 * 16:x1 * 16] = 0


def lift(img, walk, mats, x0=0, x1=None):
    """Lift the mat (its cells all on one row, under the floor) onto the floor's last row, and the warps with it.
    Returns (mats, walk), the mats one row up; the row they left is black and not walked on."""
    rows = {y for _, y in mats}
    assert len(rows) == 1, rows
    y = rows.pop()
    move_row(img, y, y - 1, x0, x1)
    new = {(x, y - 1) for x, _ in mats}
    return new, (set(walk) - set(mats)) | new
