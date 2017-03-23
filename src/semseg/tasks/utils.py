import numpy as np


def make_prediction_tile(full_tile, tile_size, predict):
    quarter_tile_size = tile_size // 4
    half_tile_size = tile_size // 2
    nb_prediction_channels = \
        predict(full_tile[0:tile_size, 0:tile_size, :]).shape[2]
    full_prediction_tile = np.zeros(
        (full_tile.shape[0], full_tile.shape[1], nb_prediction_channels),
        dtype=np.uint8)

    def snap_bounds(row_begin, row_end, col_begin, col_end):
        # If the tile straddles the edge of the full_tile, then
        # snap it to the edge.
        if row_end > full_tile.shape[0]:
            row_begin = full_tile.shape[0] - tile_size
            row_end = full_tile.shape[0]

        if col_end > full_tile.shape[1]:
            col_begin = full_tile.shape[1] - tile_size
            col_end = full_tile.shape[1]

        return row_begin, row_end, col_begin, col_end

    def update_prediction(row_begin, row_end, col_begin, col_end):
        row_begin, row_end, col_begin, col_end = \
            snap_bounds(row_begin, row_end, col_begin, col_end)

        tile = full_tile[row_begin:row_end, col_begin:col_end, :]
        prediction_tile = predict(tile)

        full_prediction_tile[row_begin:row_end, col_begin:col_end, :] = \
            prediction_tile

    def update_prediction_crop(row_begin, row_end, col_begin, col_end):
        row_begin, row_end, col_begin, col_end = \
            snap_bounds(row_begin, row_end, col_begin, col_end)

        tile = full_tile[row_begin:row_end, col_begin:col_end, :]
        prediction_tile = predict(tile)

        prediction_tile_crop = prediction_tile[
            quarter_tile_size:tile_size - quarter_tile_size,
            quarter_tile_size:tile_size - quarter_tile_size,
            :]

        full_prediction_tile[
            row_begin + quarter_tile_size:row_end - quarter_tile_size,
            col_begin + quarter_tile_size:col_end - quarter_tile_size,
            :] = prediction_tile_crop

    for row_begin in range(0, full_tile.shape[0], half_tile_size):
        for col_begin in range(0, full_tile.shape[1], half_tile_size):
            row_end = row_begin + tile_size
            col_end = col_begin + tile_size

            is_edge = (row_begin == 0 or row_end >= full_tile.shape[0] or
                       col_begin == 0 or col_end >= full_tile.shape[1])

            if is_edge:
                update_prediction(row_begin, row_end, col_begin, col_end)
            else:
                update_prediction_crop(row_begin, row_end, col_begin, col_end)

    return full_prediction_tile