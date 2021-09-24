@staticmethod
def align_bev_tuple(relative_poses_tuple, t_index, *bev):
    if t_index == 0:
        return bev
    ego_motion_matrix, dataAug_compensate_matrix = relative_poses_tuple
    if dataAug_compensate_matrix is not None:
        bev = list_2d_affine(bev, dataAug_compensate_matrix[:, t_index, :, :])
    output = list_2d_affine(bev, ego_motion_matrix[:, t_index, :, :])
    return output


@staticmethod
def align_bev_single_state(relative_poses_tuple, t_index, hidden_state):
    if t_index == 0:
        return hidden_state
    ego_motion_matrix, dataAug_compensate_matrix = relative_poses_tuple
    if dataAug_compensate_matrix is not None:
        hidden_state = bev_affine(
            hidden_state, dataAug_compensate_matrix[:, t_index, :, :]
        )
    output = bev_affine(hidden_state, ego_motion_matrix[:, t_index, :, :])
    return output


@staticmethod
def align_bev_tensor(relative_poses_tuple, t_index, hidden_state):
    if t_index == 0:
        return hidden_state
    ego_motion_matrix, dataAug_compensate_matrix = relative_poses_tuple
    if dataAug_compensate_matrix is not None:
        hidden_state = tensor_2d_affine(
            hidden_state, dataAug_compensate_matrix[:, t_index, :, :]
        )
    output = tensor_2d_affine(hidden_state, ego_motion_matrix[:, t_index, :, :])
    return output
