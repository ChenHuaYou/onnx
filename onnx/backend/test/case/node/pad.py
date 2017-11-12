from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np

import onnx
from .base import Base, expect


class Pad(Base):

    @staticmethod
    def export_constant_pad():
        node = onnx.helper.make_node(
            'Pad',
            inputs=['x'],
            outputs=['y'],
            mode='constant',
            value=1.2,
            paddings=[0, 0, 0, 0, 1, 2, 3, 4],
        )
        x = np.random.randn(1, 3, 4, 5).astype(np.float32)
        y = np.pad(
            x,
            pad_width=((0, 0), (0, 0), (1, 2), (3, 4)),
            mode='constant',
            constant_values=1.2,
        )

        expect(node, inputs=[x], outputs=[y],
               name='test_constant_pad')

    @staticmethod
    def export_reflection_and_edge_pad():
        for mode in ['edge', 'reflect']:
            node = onnx.helper.make_node(
                'Pad',
                inputs=['x'],
                outputs=['y'],
                mode=mode,
                paddings=[0, 0, 0, 0, 1, 1, 1, 1]
            )
            x = np.random.randn(1, 3, 4, 5).astype(np.float32)
            y = np.pad(
                x,
                pad_width=((0, 0), (0, 0), (1, 1), (1, 1)),
                mode=mode,
            )

            expect(node, inputs=[x], outputs=[y],
                   name='test_{}_pad'.format(mode))